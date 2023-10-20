from backend.camera_access import camera_access
from backend.microphone_access import microphone_access
from backend.language_model import language_model
from backend.object_finder import object_finder
from resources.secret_key import secret_key

import matplotlib.pyplot as plt

camera = camera_access(0)

camera.activate_camera()

frame = camera.get_frame()

camera.deactivate_camera()

object_finding_ai = object_finder()

masks = object_finding_ai.create_masks(frame)

cropped_objects = object_finding_ai.isolate_objects(frame, masks)

for cropped_frame in cropped_objects:
    plt.imshow(cropped_frame)
    plt.show()

"""
microphone = microphone_access()
microphone.ambient_noise_calculator()

robot = language_model(secret_key)

message = microphone.record_message()

transcribed = robot.transcribe(message)

print(transcribed)

print(robot.extract_text(robot.run_model_text(robot.pre_prompt_2, transcribed)))
"""