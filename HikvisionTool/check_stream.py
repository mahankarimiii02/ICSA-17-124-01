from cv2 import imshow, waitKey, resize, VideoCapture, INTER_AREA, destroyAllWindows

def start(username,password,ip,port) :
    def rescale_frame(frame, scale):    # works for image, video, live video
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return resize(frame, dimensions, interpolation=INTER_AREA)


    capture = VideoCapture(f'rtsp://{username}:{password}@{ip}:{port}/Streaming/Channels/101/')  # integer to capture from webcam, path to capture video file
   
    while True : 
        isTrue,frame = capture.read()
        if not isTrue : 
            pass
        else :
            frame_resized = rescale_frame(frame, scale=.4)
            imshow("Video Resized", frame_resized)
        if waitKey(20) & 0xFF == ord("q"):       # press "q" key to exit loop
            break

        
    capture.release()   # stop capturing the image/video
    destroyAllWindows() 

#start('admin','Uniview666','109.122.239.84',554)



