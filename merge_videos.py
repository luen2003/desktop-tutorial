import cv2

def merge_videos(video_paths, output_video_path):
    """
    Ghép nhiều video lại với nhau và lưu video đầu ra.

    Args:
        video_paths (list): Danh sách đường dẫn đến các video cần ghép.
        output_video_path (str): Đường dẫn đến video đầu ra.
    """

    out = None  # Khởi tạo video writer

    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            if out is None:
                # Tạo VideoWriter cho video đầu ra nếu chưa được khởi tạo
                fps = cap.get(cv2.CAP_PROP_FPS)
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

            # Kiểm tra frame hợp lệ trước khi ghi vào video đầu ra
            if frame is not None:
                out.write(frame)

        cap.release()

    if out is not None:
        out.release()

# Ví dụ sử dụng hàm merge_videos
video_paths = ['video1.mp4', 'video2.mp4']  # Danh sách đường dẫn đến các video cần ghép
output_video_path = 'output_video.mp4'  # Đường dẫn đến video đầu ra

merge_videos(video_paths, output_video_path)