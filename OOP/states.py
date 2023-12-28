# Maintaining states within the class
class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording 

    def record(self):
        if self.recording:
            print(f'{self.name} is  already recording...')
            return

        print(f'{self.name} is recording...')
        self.recording = True

    def stop_record(self):
        if not self.recording:
            print(f'{self.name} is not recording...')
            return
        
        print(f'{self.name} has stopped recording...')
        self.recording = False

    def photograph(self):
        if self.recording:
            print(f"{self.name} can't take pictures while recording.")
            return
        
        print(f"{self.name} is taking a picture...")

camera_one = Camera('Canon')
camera_two = Camera('Sony')

camera_one.record()
camera_one.record()
camera_one.photograph()
camera_one.stop_record()
camera_one.photograph()
#print(camera_one.recording)
#print(camera_two.recording)