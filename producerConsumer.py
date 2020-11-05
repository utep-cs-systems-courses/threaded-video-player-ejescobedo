#!/usr/bin/env python3

import cv2
import os
import time

clipFileName = "clip.mp4"
capacity = 10

readFramesQueue = Queue(capacity)
grayFramesQueue = Queue(capacity)

def extractFrames(clipFileName, readFramesQueue):
    vidcap = cv2.VideoCapture(clipFileName)
    # create the output directory if it doesn't exist
    # read one frame

    success,image = vidcap.read()
    print(f'Reading frame {count} {success}')
    while success and count < 72:
        # write the current frame out as a jpeg image
        #TODO change it to enqueue to readFramesQueue
        cv2.imwrite(f"{outputDir}/frame_{count:04d}.bmp", image)
        success,image = vidcap.read()
        print(f'Reading frame {count}')
        count += 1


def convertToGrayScale(readFramesQueue, grayFramesQueue):
    # initialize frame count
    count = 0

    # get the next frame file name
    
    #TODO change it to load from the readFramesQueue
    inFileName = f'{outputDir}/frame_{count:04d}.bmp'
    # load the next file
    inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)



    while inputFrame is not None and count < 72:
        print(f'Converting frame {count}')

        # convert the image to grayscale
        grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)

        #change it to enqueue into the grayFramesQueue
        cv2.imwrite(outFileName, grayscaleFrame)
        count += 1

        # generate input file name for the next frame
        #TODO change it to dequeue from readFramesQueue
        inFileName = f'{outputDir}/frame_{count:04d}.bmp'
        # load the next frame
        inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

def displayFrames(grayFramesBuffer):
    # initialize frame count
    count = 0



    # Generate the filename for the first frame
    #TODO change to read/dequeue from the grayFramesBuffer
    frameFileName = f'{outputDir}/grayscale_{count:04d}.bmp'
    # load the frame
    frame = cv2.imread(frameFileName)

    while frame is not None:
        print(f'Displaying frame {count}')

        # Display the frame in a window called "Video"
        cv2.imshow('Video', frame)

        # Wait for 42 ms and check if the user wants to quit
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break

        # get the next frame filename
        count += 1

        #TODO dequeue from grayFramesBuffer the next frame
        frameFileName = f'{outputDir}/grayscale_{count:04d}.bmp'
        # Read the next frame file
        frame = cv2.imread(frameFileName)

    # make sure we cleanup the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()
