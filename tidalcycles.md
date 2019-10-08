= Prerequisites =

The prerequisites require recent versions of Tidal and SuperDirt:

* Upgrade to the latest Tidal (this post assumes version 0.9.10 or greater)</li>
* Make sure you have the latest SuperDirt quark. Uninstalling and reinstalling the SuperDirt quark might be easiest. See [https://github.com/supercollider-quarks/quarks](github.com/supercollider-quarks/quarks) for details on how to update Quarks.

= Usage =
To begin, you'll start in SuperCollider. Start up SuperDirt as you normally would. Then, in SuperCollider eval the following code:

<source>
MIDIClient.init;
</source>

You should now see a list of the system MIDI devices in SuperCollider's post window. The output will look something like this:

<source>
MIDI Sources:
	MIDIEndPoint("LoopBe Internal MIDI", "LoopBe Internal MIDI")
	MIDIEndPoint("Focusrite USB MIDI", "Focusrite USB MIDI")
MIDI Destinations:
	MIDIEndPoint("Microsoft GS Wavetable Synth", "Microsoft GS Wavetable Synth")
	MIDIEndPoint("LoopBe Internal MIDI", "LoopBe Internal MIDI")
	MIDIEndPoint("Focusrite USB MIDI", "Focusrite USB MIDI")
</source>

Take note that these MIDI devices have ''two'' parts to their names. You will need both parts in the next step, which is to actually connect to the MIDI device. Eval the following line:

<source>
~midiOut = MIDIOut.newByName("Focusrite USB MIDI", "Focusrite USB MIDI"); // substitute your own device here
</source>

Above, we have stored a reference to the device in a variable named <code>~midiOut</code>.

Finally, define the name of the "synth" in Tidal you will use to control this device. Below, we will call it "midi". Eval the following line:

<source>
~dirt.soundLibrary.addMIDI(\midi, ~midiOut);
</source>

Optionally, you can define a latency value on your device:

<source>~midiOut.latency = 0.45;</source>

That's it for initialization. You should now have a MIDI device connected in SuperDirt, running as a synth named "midi".

= Usage in Tidal =

== Note Patterns ==

Now we can start writing some Tidal patterns to control the MIDI device. Let's send it a trivial note pattern:

<source>
d1 $ n "0 2 4 7" # s "midi"
</source>

That should play a simple four-note pattern. Notice we're just using the synth name "midi" to send notes to the MIDI device.

You can also use the note-name and octave notation:

<source>
d1 $ n "c4 d4 e5 g3" # s "midi"
</source>

== MIDI Channels ==

The default MIDI channel is 1. SuperDirt MIDI channels are indexed starting at zero, so MIDI channel 1 is <code>midichan 0</code>:

<source>
d1 $ note "0 2 4 7" # s "midi" # midichan 0
</source>

If your synth is listening on a different channel, let's say, MIDI channel 5, you would use <code>midichan 4</code>:

<source>
d1 $ note "0 2 4 7" # s "midi" # midichan 4
</source>

Notice that <code>midichan</code> accepts a pattern of numbers, so you can use a pattern to play on different MIDI channels:

<source>
d1 $ note "0 2 4 7" # s "midi" # midichan "0 4"
</source>

The above pattern plays notes "0 2" on channel 1 and "4 7" on channel 5.

== CC Params ==

To send a CC param to your synth, the best way to do it in the new SuperDirt MIDI is with a different Tidal pattern. To create this pattern, you'll be using
two new SuperDirt MIDI params:

* <code>ccn</code> - the CC param number you want to control: <code>ccn 30</code>
* <code>ccv</code> - the value to send to the CC param, ranging from 0 to 127: <code>ccv 64</code>

Here's a full example, sending a value of 64 to CC param 30:

<source>
d2 $ ccv 64 # ccn 30 # s "midi"
</source>

You can of course also specify the MIDI channel with <code>midichan</code>:

<source>
d2 $ ccv 64 # ccn 30 # s "midi" # midichan 4
</source>

You can specify patterns of CC values:

<source>
d2 $ ccv "20 40 60 80 100" # ccn 30 # s "midi"
</source>

<source>
d2 $ ccn "30*4" # ccv (range 20 100 $ slow 30 sine) # s "midi"
</source>

Note that the left-most pattern defines the rhythm in this case when using <code>#</code>.

If you have a specific feature on your device that listens on a specific CC number, you can give it a friendly name if you wish:

<source>
let ringMod = 30
d2 $ ccv "0 20 50 60" # ccn ringMod # s "midi"
</source>

If you have many CC params you want to control at once, a <code>stack</code> works well:

<source>
d2 $ density 8 $ stack [
  ccn 30 # ccv (range 0 127 $ slow 30 sine),
  ccn 31 # ccv "[0 70 30 110]/3",
  ccn 32 # ccv 10 
  ] # s "midi"
</source>

= MIDI Clock =

See the [[MIDI Clock]] page.
