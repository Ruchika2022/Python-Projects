import cv2 as cv
def main():
    # Import video files, parameters: 0 comes with a camera, 1 USB camera, read the video file when the file name is
    video_caputre = cv.VideoCapture("yt.mp4")
 
         # Get the parameters of the imported video
    fps = video_caputre.get(cv.CAP_PROP_FPS)
    width = video_caputre.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_caputre.get(cv.CAP_PROP_FRAME_HEIGHT)
 
    print("fps:", fps)
    print("width:", width)
    print("height:", height)
 
         # Define the intercept size, the h and w of each frame defined later must be consistent here, otherwise the video cannot be played
         # Note here is the height (height, width)
    size = (int(height), int(width / 2))
 
         # Create video writing object
    videp_write = cv.VideoWriter("videoFrameTarget.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
 
         # Read the video frame, then write the file and display it in the window
    success, frame_src = video_caputre.read()
    while success and not cv.waitKey(1) == 27: #Exit after reading or press esc to exit
 
                 # [width, height] To be consistent with the size parameter defined above, pay attention to the position of the parameter
            frame_target = frame_src[0:int(width/2), 0:int(height)]
                 # Write video file
            videp_write.write(frame_target)
 
                 # Display the cropped video and the original video
            cv.imshow("video", frame_target)
            cv.imshow("Video_src", frame_src)
 
                 # Keep reading
            success, frame_src = video_caputre.read()
 
    print("Video cropping completed")
 
         # Destroy the window, release resources
    cv.destroyWindow("video")
    cv.destroyWindow("Video_src")
    video_caputre.release()
 
 
if __name__=="__main__":
    main()