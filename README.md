This is the [PocketSphinx](https://pocketsphinx.readthedocs.io/) Python library sample code configured to run in pdm.

Sample usage (on big endian systems substitute s16le for s16be):

    pdm install
    ffmpeg -y -i File\ Downloaded\ From\ YouTube.f251.webm -f s16le -acodec pcm_s16le output.raw
    # If the file is stereo, manually convert to mono here. Use Audacity or -map_channel 0.0.0
    time pdm run platform_test -- --samplerate 48000 output.raw > test.txt

This will produce a transcript of the input file, but in my testing not a very good one.

These files may be taken as Creative Commons Zero licensed.
