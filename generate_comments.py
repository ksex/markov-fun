from PIL import Image
from Trainer import DataTrainer, ImageSequencer
from Stepper import Stepper


trainer = DataTrainer()
stepper = Stepper()

raw_file = open("data/training/code-comments/comments.txt", 'r')
raw_data = raw_file.read()
raw_file.close()

x = trainer.train_text_data(
        raw_text = raw_data,
        order = 1,
        )

phrase = stepper.new_phrase(
            model = x,
            eol = 'EOL',
            punc = ['!', '.', '?'])

print(phrase)
