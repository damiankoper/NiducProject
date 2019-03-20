from Generators.AudioDataGenerator import AudioDataGenerator

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
generator.plotData(filename="plots/guitar")
