import numpy as N
import wave, subprocess

def nat_to_vn(nat):
	try:
		integer = int(nat)
	except ValueError:
		return ""
	if integer < 0:
		return ""
	
	emptyset = "{}"
	
	if integer == 0:
		return "{}"
	if integer > 0:
		l = ["" for i in xrange(integer)]
		l[0] = "{}"
		
		for i in xrange(integer-1):
			l[i+1] = "{%s}" % ",".join(l[0:i+1])
		
		return "{" + ",".join(l) + "}"

def ordered_pair(p,q):
	'''weiner definition (a,b) = {{{a},{}},{{b}}}'''
	return "{{{%s},{}},{{%s}}}" % (p,q)
	
def int_to_vn(integer):
	'''{p,q} is p~q, where p and q are ordered pairs of the form (a,b) where a,b are natural numbers and a-b = N'''
	
	#N = 0 means (0,0) ~ {1,1}   
	if integer == 0:
		p = ordered_pair(nat_to_vn(0),nat_to_vn(0))
		q = ordered_pair(nat_to_vn(1),nat_to_vn(1))
		return "{%s,%s}" % (p,q)

	#Positive N is (N,0) ~ (N+1,1)
	if integer > 0:
		p = ordered_pair(nat_to_vn(integer),nat_to_vn(0))
		q = ordered_pair(nat_to_vn(integer+1),nat_to_vn(1))
		return "{%s,%s}" % (p,q)
		
	#Negative N is (0,N) ~ (1,N+1)
	if integer < 0:
		p = ordered_pair(nat_to_vn(0),nat_to_vn(-1 * integer))
		q = ordered_pair(nat_to_vn(1),nat_to_vn((-1 * integer) + 1))
		return "{%s,%s}" % (p,q)

def q_to_vn(q1,q2):
	'''{m,n} is m~n where m and n are ordered pairs such that m1*n2 - m2*n1 = 0 for integer m,n'''
	
	#Division by 0 zero
	if q2 == 0 and q1 !=0:
		return ""
		
	#Q = 0 means (0,0) ~ {1,1} | 0*1 - 1*0 = 0
	if q1 == 0:
		m = ordered_pair(int_to_vn(0),int_to_vn(0))
		n = ordered_pair(int_to_vn(1),int_to_vn(1))
		return "{%s,%s}" % (m,n)
	
	#Otherwise q1,q2 = m1,m2, (q1,q2) ~ (-q1,q2) | q1*-q2 - -q1*q2 = 0
	else:
		m = ordered_pair(int_to_vn(q1),int_to_vn(q2))
		n = ordered_pair(int_to_vn(-q1),int_to_vn(-q2))
		return "{%s,%s}" % (m,n)
		
		
##############

class SoundFile:
	def __init__ (self):
		self.file = wave.open('temp.wav', 'wb')
		self.sr = 44100
		self.file.setparams((1, 2, self.sr, 44100*4, 'NONE', 'noncompressed'))

	def write(self,signal):
		self.file.writeframes(signal)

	def close(self):
		self.file.close()

def prepare_signal(freq):

	def sine(x):
		return VOL * N.sin(x)

	def organ(x, no):
		base = 0
		for k in xrange(no):
			M = 2**(k)
			base = base + VOL/M * N.sin(M * xaxis)
		return base

	def evenorgan(x, no):
		base = 0
		for k in xrange(no):
			if k%2:
				M = 2**(k)
				base = base + VOL/M * N.sin(M * xaxis)
		return base

	def oddorgan(x, no):
		base = 0
		for k in xrange(no):
			if not k%2:
				M = 2**(k)
				base = base + VOL/M * N.sin(M * xaxis)
		return base

	def saworgan(x, no):
		base = 0
		for k in xrange(no):
			M = 2**(k)
			base = base + VOL/(N.exp(xaxis/2)*M) * N.sin(M * xaxis)
		return base

	# let's prepare signal
	duration = NOTELENGTH
	samplerate = 44100 # Hz
	samples = duration*samplerate
	frequency = freq # 440 Hz
	period = samplerate / float(frequency) # in sample points
	omega = N.pi * 2 / period

	xaxis = N.arange(int(period),dtype = N.float) * omega

	timbredict = {"sine": sine(xaxis),
			"organ": organ(xaxis,TIMBRETERMS),
			"oddorgan": oddorgan(xaxis,TIMBRETERMS),
			"evenorgan": evenorgan(xaxis,TIMBRETERMS),
			"saworgan": evenorgan(xaxis,TIMBRETERMS)}

	ydata = timbredict[TIMBRE]

	signal = N.resize(ydata, (samples,))

	ssignal = ''
	for i in range(len(signal)):
		ssignal += wave.struct.pack('h',signal[i]) # transform to binary
	return ssignal


def go_up(last):
	out = last*(UP)**NUMHTONES
	return out

def go_down(last):
	out = last*(DOWN)**NUMHTONES
	return out

def repeat(last):
	return last

BASE = 110 #Hz
TET = 12
NUMHTONES = 2
NOTELENGTH = 0.2 #secs
TIMBRE = "saworgan"

TIMBRETERMS = 12
VOL = 16384
UP = float(2) ** (float(1)/float(TET))
DOWN = float(1)/UP #1/(2^(1/12))


tones = [BASE]

ruledict = {"u":go_up, "d":go_down, "r":repeat }

num = raw_input("What number would you like to musicalise?\nPlease input an integer or rational number (n/m)\n> ")

if "/" in num:
		nums = num.split("/")
		nume, denom = int(nums[0]), int(nums[1])
		if nume > 10:
			print("Numerator and/or denominator too large (greater than 10)")
			quit()
		elif denom > 10:
			print("Denominator and/or denominator too large (greater than 10)")
			quit()
		else:
			print("lol")
			notestring = q_to_vn(nume,denom)

else:
		if int(num) > 10:
			print("Too large (greater than 10)")
			quit()

		if int(num) < -10:
			print("Too small (less than -10)")
			quit()

		elif int(num) == 0:
			print("Ok.\n(no sound 4 u)")
			quit()

		else:
			notestring = int_to_vn(int(num))


dirlist = ["r"]

for note in notestring:

	if note == "{":
		dirlist = dirlist + ["u"]
	if note == "}":
		dirlist = dirlist + ["d"]
	if note == ",":
		dirlist = dirlist + ["r"]
	else:
		pass
	
tone = BASE
for rule in dirlist:
	tone = ruledict[rule](tone)
	tones.append(tone)


wav = SoundFile()

for tone in tones:
	wav.write(prepare_signal(tone))
wav.close()

if "/" in num:
	tnum = "%sover%s" % (nume,denom)
else:
	tnum = num

wav = 'temp.wav' % (tnum, TET, BASE, NUMHTONES, NOTELENGTH, TIMBRE)
mp3 = 'peano-%s-%sTET-%sHz-%sst-%ss-%s.mp3' % (tnum, TET, BASE, NUMHTONES, NOTELENGTH, TIMBRE)
cmd = 'lame --preset fast medium %s %s' % (wav, mp3)
clr = 'rm %s' % wav

try:
	subprocess.check_output(cmd, shell=True)
	subprocess.call(clr, shell=True)
except:
	print("Could not convert to mp3. Please try installing lame (and/or lunix lol) and see temp.wav for output. NB. Filename would have been %s" % mp3)

print notestring








