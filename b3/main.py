from data.flights import flights
from core.logistics import display_flights
from core.manager import add_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_log_folder

def main():
    while True:
        print("""
===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====
1. Hiển thị lịch trình và Thống kê hậu cần
2. Tiếp nhận chuyến bay mới
3. Tính thời gian hạ cánh dự kiến (ETA)
4. Khởi tạo thư mục lưu trữ log hệ thống
5. Thoát chương trình
==================================================""")
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice == 1:
                display_flights(flights)
            elif choice == 2:
                add_flight(flights)
            elif choice == 3:
                calculate_eta(flights)
            elif choice == 4:
                create_log_folder()
            elif choice == 5:
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            else:
                print("Vui lòng nhập lựa chọn từ 1 đến 5.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số từ 1 đến 5!")

if __name__ == "__main__":
    main()
