import cv2

class camera_access:

    """
    The `CameraAccess` class provides a convenient interface to access and manage cameras using OpenCV (cv2).

    Attributes:
        number_of_cameras (int): The total number of camera instances created.
        number_of_activated_cameras (int): The number of cameras currently activated.
        maximum_cameras (int): The maximum number of cameras supported.

    Methods:
        __init__(self, camera_number): Initializes a camera instance with the specified camera number.
        activate_camera(self): Activates the camera by opening the capture device.
        deactivate_camera(self): Deactivates the camera by releasing the capture device.
        get_camera_properties(self): Retrieves the camera properties like FPS, width, and height.
        get_frame(self): Captures and returns a frame from the camera.
        get_available_cameras(): Returns a list of available camera indexes.

    """

    number_of_cameras = 0
    number_of_activated_cameras = 0
    maximum_cameras = 10

    def __init__(self, camera_number):
        """
        Initializes a camera instance with the specified camera number.

        Args:
            camera_number (int): The camera index or ID to access.
        """
        self.camera_number = camera_number
        self.fps = None
        self.width = None
        self.height = None
        self.capture = None
        camera_access.number_of_cameras += 1

    def activate_camera(self):
        """
        Activates the camera by opening the capture device.
        """
        if self.capture is None or not self.capture.isOpened():
            self.capture = cv2.VideoCapture(self.camera_number)
            camera_access.number_of_activated_cameras += 1

    def deactivate_camera(self):
        """
        Deactivates the camera by releasing the capture device.
        """
        if self.capture is not None and self.capture.isOpened():
            self.capture.release()
            camera_access.number_of_activated_cameras -= 1

    def get_camera_properties(self):
        """
        Retrieves the camera properties like FPS, width, and height.

        """
        if self.capture is not None and self.capture.isOpened():
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)
            self.width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
    def get_frame(self):
        """
        Captures and returns a frame from the camera.

        Returns:
            numpy.ndarray: The captured frame as a NumPy array.

        """
        if self.capture is not None and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                return frame
            
        return None

    @staticmethod
    def get_available_cameras():
        cameras_available = []
        for camera_index in range(camera_access.maximum_cameras):
            capture = cv2.VideoCapture(camera_index)
            if capture.isOpened():
                cameras_available.append(camera_index)
                capture.release()

        return cameras_available

