import cv2
import time
import os

def video_to_all_frames(input_loc, output_loc, filename, movie_num):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        name_of_file = "/" + filename[:4] + "_" + str(movie_num) + "_%#05d.jpg" % (count+1)
        print(name_of_file)
        cv2.imwrite(output_loc + name_of_file, frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break

def video_to_each_nth_frames(input_loc, output_loc, filename, movie_num, n):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)

    nums = range(video_length)
    list_of_frames = []

    for i in range(0, len(nums)+1, n):
        list_of_frames.append(i)

    if(video_length%n > 0):
        list_of_frames.append(video_length)

    print(list_of_frames)

    print ("Converting video..\n")
    # Start converting the video
    count = 0
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        if (count in list_of_frames):
            name_of_file = "/" + filename[:4] + "_" + str(movie_num) + "_%#05d.jpg" % (count)
            print(name_of_file)
            cv2.imwrite(output_loc + name_of_file, frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break


if __name__=="__main__":

    # # for the whole folders, set path_to_start to the upper folder with movies
    # path_to_start = 'C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\dataset\\LSMDC - short\\frames\\movies\\'
    # for movie_folder in os.listdir(path_to_start):
    #     path_temp = os.path.join(path_to_start, movie_folder)
    #     movie_num = 1
    #     for filename in os.listdir(path_temp):
    #         if (filename.endswith(".avi")):  # or .avi, .mpeg, whatever.
    #             input_loc = path_temp + '\\' + filename
    #             output_loc = 'C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\dataset\\LSMDC - short\\frames\\extracted\\' + movie_folder + '\\'
    #             # video_to_all_frames(input_loc, output_loc, filename, movie_num)
    #             video_to_each_nth_frames(input_loc, output_loc, filename,movie_num,  5)
    #             movie_num = movie_num + 1
    #         else:
    #             continue

        # for one folder with avi files
    path_temp = 'D:\\Yulia\\dataset\\0001_American_Beauty'

    file_num = 1
    for filename in os.listdir(path_temp):
        if (filename.endswith(".avi")):  # or .avi, .mpeg, whatever.
            input_loc = path_temp + '\\' + filename
            output_loc = 'D:\\Yulia\\frames\\1' + '\\'
            # video_to_all_frames(input_loc, output_loc, filename, movie_num)
            video_to_each_nth_frames(input_loc, output_loc, filename, file_num, 5)
            file_num = file_num + 1
        else:
            continue