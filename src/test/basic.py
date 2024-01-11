from pocketsphinx import AudioFile
import click

@click.command(help="Emit hg commands to archive a directory tree created by backup.py")
@click.argument('infile', type=click.Path(exists=True))
@click.option('--samplerate', '-s', type=click.FLOAT, default=16000)
def run(infile, samplerate):
	for phrase in AudioFile(infile, samprate=samplerate):
		print(phrase)
