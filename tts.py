def texttospeech1(string, voice, audio_config, hello=None):
    # Set the text input to be synthesized
    sample=hello+string

    synthesis_input = texttospeech.types.SynthesisInput(text=sample)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    player = vlc.MediaPlayer("output.mp3")
    player.play()
    player.stop()
