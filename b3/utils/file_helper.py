import os

def create_log_folder():
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    folder_name = "aviation_logs"
    if os.path.exists(folder_name):
        print("[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo.")
    else:
        print("[SYSTEM] Thư mục 'aviation_logs' chưa tồn tại.")
        print("[SYSTEM] Đang tiến hành khởi tạo...")
        os.mkdir(folder_name)
        print("[SYSTEM] Tạo thư mục thành công!")
