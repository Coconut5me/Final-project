import array as arr #Để gọi hàm tạo mảng
import time  #Để gọi time.sleep(n) (màn hình chờ n giây rồi chạy tiếp )
from clear_screen import clear  #Để gọi clear(): xóa màn hình

#Mấy cái def này là mấy cái hàm để xíu vào chương trình gọi cho đỡ rối với cả có1 thể tái sử dụng
def menu():       # sau chữ def là tên của hàm. VD: tên hàm ở đây là menu.
	print("1. Nhập")    #để đơn giản thì tất cả hàm ở đây đều không có đầu vào lẫn kh có trả về.
	print("2. Xuất")
	print("0. Thoát")
def nhap():
	print("1. Nguồn thu")
	print("2. Nguồn chi")
	print("0. Quay về")
def nguon_thu():
	print("1. Lương")
	print("2. Thu nhập khác")
def nguon_chi():
	print("1. Khoản tiền cần thiết (50%)")
	print("2. Khoản đầu tư tiết kiệm (20%)")
	print("3. Khoản giải trí (30%)")
def canthiet():
	print("1. Hóa đơn tiện ích")
	print("2. Ăn uống")
	print("3. Di chuyển")
	print("4. Y tế")
	print("5. Đồ gia dụng / đồ dùng cá nhân")
	print("6. Các chi phí khác")
def tietkiem():
	print("1. Mua nhà")
	print("2. Gửi ngân hàng")
	print("3. Giáo dục")
	print("4. Các khoản khác")
def giaitri():
	print("1. Du lịch")
	print("2. Xem phim")
	print("3. Làm đẹp")
	print("4. Quà tặng")
	print("5. Các loại hình dịch vụ khác")
def xuat():
	print("1. Chi tiêu trong tháng vừa rồi")
	print("2. Số tiền đã tiết kiệm được")
	print("0. Quay về")


#tạo sẵn mảng a, b, c để xíu nữa chứa dữ liệu của nguồn chi
a=arr.array('i', [0, 0, 0, 0, 0, 0, 0])
b=arr.array('i', [0, 0, 0, 0, 0])
c=arr.array('i', [0, 0, 0, 0, 0, 0])

#Này là khởi tạo mấy cái biến 
flag = 0
S = 0
sum_a = 0
sum_b = 0
sum_c = 0
sum = 0
du = 0
tiendautu = 0

menu() #Gọi hàm menu
option = int(input("Bạn muốn nhập hay xuất dữ liệu? ")) #Lấy giá trị vào biến option
print()


while option != 0: #Trả về trang ban đầu
	if option == 1: #Bắt đầu nhập
		nhap() #Gọi hàm nhap
		x = int(input("Bạn muốn nhập dữ liệu nào? "))
		print()
		if x == 1:
			nguon_thu() #Gọi hàm nguon_thu
			y = int(input("Khoản thu đến từ? "))
			print()
			if y == 1:
				l = int(input("Hãy nhập lương của bạn: "))
				S = S + l
				flag = 1
				print()
			elif y == 2:
				tn = int(input("Hãy nhập thu nhập khác của bạn: "))
				S = S + tn
				flag = 1
				print()
			else: print("Không có lựa chọn này.")
		if x == 2:
			chi = int(input("Bạn muốn chi bao nhiêu tiền? "))
			print()
			nguon_chi() #Gọi hàm nguon_chi
			print("0. Quay lại")
			y = int(input("Khoản chi dành cho mục đích? "))
			print()
			if y == 1:
				canthiet() #Gọi hàm canthiet
				i = int(input("Cụ thể? "))
				a[i] = a[i] + chi
				print()
				flag = 1
			elif y == 2:
				tietkiem() #Gọi hàm tietkiem
				i = int(input("Cụ thể? "))
				b[i] = b[i] + chi
				print()
				flag = 1
			elif y == 3:
				giaitri() #Gọi hàm giaitri
				i = int(input("Cụ thể? "))
				c[i] = c[i] + chi
				print()
				flag = 1
			else: print("Không có lựa chọn này.")





	elif option == 2: #Bắt đầu Xuất
		xuat() #Gọi hàm xuat
		x = int(input("Bạn muốn xuất dữ liệu nào? "))
		if x == 1:
			nguon_chi() #Gọi hàm nguon_chi
			print("4. Tổng số tiền đã chi")
			print("0. Quay lại")
			y = int(input("Bạn muốn xuất khoản chi tiêu nào?"))
			print()
			if y == 1:
				canthiet() #Gọi hàm canthiet
				i = int(input("Cụ thể? "))
				print("Bạn đã chi cho mục",i ,": ",a[i], "VNĐ")
				print()
			elif y == 2:
				tietkiem() #Gọi hàm tietkiem
				i = int(input("Cụ thể? "))
				print("Bạn đã chi ", i,": ",b[i], "VNĐ")
				print()
			elif y == 3:
				giaitri() #Gọi hàm giaitri
				i = int(input("Cụ thể? "))
				print("Bạn đã chi ",i,": ",c[i], "VNĐ")
				print()
			elif y == 4:
				if flag == 1: #Kỹ thuật đặt cờ, để tránh khi mình chưa nhập dữ liệu mới mà vòng lặp vẫn chạy lại
					sum_a = 0
					sum_b = 0
					sum_c = 0
					for i in range(1, len(a)):        #Vòng lặp for này để tính tổng từng khoản A, B, C
						sum_a = sum_a + a[i]
					for i in range(1, len(b)):
						sum_b = sum_b + b[i]
					for i in range(1, len(c)):
						sum_c = sum_c + c[i]
					sum = sum_a + sum_b + sum_c #Tính tổng số tiền
					flag = 0
				elif flag == 2:
					sum_a = 0
					sum_b = 0
					sum_c = 0
					for i in range(1, len(a)):
						sum_a = sum_a + a[i]
					for i in range(1, len(b)):
						sum_b = sum_b + b[i]
					for i in range(1, len(c)):
						sum_c = sum_c + c[i]
					sum = sum_a + sum_b + sum_c
					sum = sum + du
					du = S - sum
					flag = 0
				print("Tổng số tiền đã chi là:", sum , "VNĐ")
				print()
				print("Lời khuyên chi tiêu: ")  #Đưa ra lời khuyên chi tiêu
				if ((sum_a/sum) >= 0.47) and ((sum_a/sum) <= 0.53) and ((sum_b/sum) >= 0.17) and ((sum_b/sum) <= 0.23) and ((sum_c/sum) >= 0.27) and ((sum_c/sum) <= 0.33):
					print("Bạn có kế hoạch chi tiêu tuyệt vời!")
				else:
					if ((sum_a / sum) > 0.53) and ((sum_c / sum) > 0.33) :
						print("Bạn nên điều chỉnh lại kế hoạch chi tiêu bản thân và bớt ăn chơi đi!")
					elif ((sum_a / sum) > 0.53) :
						print("Bạn cần có kế hoạch chi tiêu tốt hơn!")
					elif ((sum_c / sum) > 0.33):
						print("Bạn càn bớt ăn xài lại!")
					else:
						print("Bạn cần có kế hoạch chi tiêu tối ưu hơn!")
				time.sleep(2)
			else: print("Không có lựa chọn này.")


		elif x == 2:
			if flag == 1: #Kỹ thuật đặt cờ, để tránh khi mình chưa nhập dữ liệu mới mà vòng lặp vẫn chạy lại
				sum_a = 0
				sum_b = 0
				sum_c = 0
				for i in range(1, len(a)):
					sum_a = sum_a + a[i]
				for i in range(1, len(b)):
					sum_b = sum_b + b[i]
				for i in range(1, len(c)):
					sum_c = sum_c + c[i]
				sum = sum_a + sum_b + sum_c
				du = S - sum
				flag = 0
			elif flag == 2:
				sum_a = 0
				sum_b = 0
				sum_c = 0
				for i in range(1, len(a)):
					sum_a = sum_a + a[i]
				for i in range(1, len(b)):
					sum_b = sum_b + b[i]
				for i in range(1, len(c)):
					sum_c = sum_c + c[i]
				sum = sum_a + sum_b + sum_c
				sum = sum + du
				du = S - sum
				flag = 0
			print("Thu nhập:", S, "VNĐ")
			print("Đã chi:", sum, "VNĐ")
			if du > 0 :
				print("Số tiền tiết kiệm được: ", du, "VNĐ")
				print("Bạn có muốn cho vào quỹ đầu từ không?")
				print("1. Có")
				print("2. Không")
				dautu = int(input())
				if dautu == 1:
					print("Chúc mừng bạn đã có khoản đầu tư mới!")
					tiendautu = tiendautu + du   #Tiền dư sẽ chuyển thành tiền đã đầu tư
					print("Bạn đã đầu tư tổng cộng:",tiendautu,"VNĐ")
					flag = 2
				else:
					print("Bạn chắc chứ?")
					print("1. Không, tôi muốn đầu tư.")
					print("2. Tôi chắc chắn.")
					dautu = int(input())
					if dautu == 1:
						print("Chúc mừng bạn đã có khoản đầu tư mới!")
						tiendautu = tiendautu + du
						print("Bạn đã đầu tư tổng cộng:",tiendautu,"VNĐ")
						flag = 2
					elif dautu == 2:
						print("Cảm ơn bạn đã sử dụng dịch vụ")
					else: print("Không có lựa chọn này.")
			elif du < 0:
				du = (-1) * du
				print("Bạn đang nợ", du, "VNĐ" )
			time.sleep(2)
	

	else:
		print("Không có lựa chọn, hãy chọn lại! ")

	print()
	time.sleep(2)
	clear()
	menu()
	option = int(input("Bạn muốn nhập hay xuất dữ liệu? "))
	print()


