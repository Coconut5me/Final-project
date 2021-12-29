import time  #Để gọi time.sleep(n) (màn hình chờ n giây rồi chạy tiếp )
from clear_screen import clear  #Để gọi clear(): xóa màn hình


#Mấy cái def này là mấy cái hàm để xíu vào chương trình gọi cho đỡ rối với cả có thể tái sử dụng
def menu():       # sau chữ def là tên của hàm. VD: tên hàm ở đây là menu.
	print('''
		1. Nhập   
		2. Xuất
		0. Thoát
		''')
def nhap():
	print('''
		1. Nguồn thu
		2. Nguồn chi
		0. Quay về
	''')
def nguon_thu():
	print('''
		1. Lương
		2. Thu nhập khác''')
def nguon_chi():
	print('')
	print('		1. Khoản tiền cần thiết (50%)')
	print('		2. Khoản đầu tư tiết kiệm (20%)')
	print('		3. Khoản giải trí (30%)')
def canthiet():
	print('''
		1. Hóa đơn tiện ích
		2. Ăn uống
		3. Di chuyển
		4. Y tế
		5. Đồ gia dụng / đồ dùng cá nhân
		6. Các chi phí khác
	''')
def tietkiem():
	print('''
		1. Mua nhà
		2. Gửi ngân hàng
		3. Giáo dục
		4. Các khoản khác
	''')
def giaitri():
	print('''
		1. Du lịch
		2. Xem phim
		3. Làm đẹp
		4. Quà tặng
		5. Các loại hình dịch vụ khác
	''')
def xuat():
	print('''
		1. Chi tiêu trong tháng vừa rồi
		2. Số tiền đã tiết kiệm được
		0. Quay về
	''')

def cuthenhapthu(t,i):
	try:
		a = int(input('	Hãy nhập '+tenthu[i]+' của bạn: '))
	except:
		a = int(input('	Nhập lại số tiền: '))
	t[i] = t[i] + a
def cuthenhapchi(a):
	i = int(input("	Cụ thể? "))
	a[i] = a[i] + chi
def cuthexuat(a):
	i = int(input("	Cụ thể? "))
	print("	Bạn đã chi cho mục",i,": ",a[i], "VNĐ")

#tạo list chứa nguồn thu
tenthu = ['lương','thu nhập khác']
t=[0,0]
#tạo list a, b, c để chứa dữ liệu của nguồn chi
a=[0, 0, 0, 0, 0, 0, 0]
b=[0, 0, 0, 0, 0]
c=[0, 0, 0, 0, 0, 0]

#Này là khởi tạo mấy cái biến
tiendautu = 0

print()
print('	   		---------------------------------------')
print('			|^_^ CHƯƠNG TRÌNH QUẢN LÝ CHI TIÊU ^_^|')
print('			---------------------------------------')
print('''
	"Người ta giàu vì biết lao động, giàu hơn nữa vì biết tiết kiệm"
						___ Ngạn ngữ Thổ Nhĩ Kỳ___
''')
time.sleep(2)
clear()
menu() #Gọi hàm menu
option = int(input("	Bạn muốn nhập hay xuất dữ liệu? ")) #Lấy giá trị vào biến option
while option<0 or option>2:
	option = int(input("	Vui lòng nhập lại: "))

while option != 0: #Trả về trang ban đầu
	if option == 1: #Bắt đầu nhập
		nhap() #Gọi hàm nhap
		print('')
		x = int(input("	Bạn muốn nhập dữ liệu nào? "))
		while x < 0 or x > 2:
			x = int(input("	Vui lòng nhập lại: "))
		if x == 1:
			nguon_thu() #Gọi hàm nguon_thu
			y = int(input("	Khoản thu đến từ? "))
			while y < 0 or y > 2:
				y = int(input("	Vui lòng nhập lại: "))
			if y == 1:
				cuthenhapthu(t,0)
			elif y == 2:
				cuthenhapthu(t,1)
			else: break
		if x == 2:
			try:
				chi = int(input("	Bạn muốn chi bao nhiêu tiền? "))
			except:
				chi = int(input("	Nhập lại số tiền: "))
			nguon_chi() #Gọi hàm nguon_chi
			y = int(input("	Khoản chi dành cho mục đích? "))
			while y < 0 or y > 3:
				y = int(input("	Vui lòng nhập lại: "))
			if y == 1:
				canthiet() #Gọi hàm canthiet
				cuthenhapchi(a)
			elif y == 2:
				tietkiem() #Gọi hàm tietkiem
				cuthenhapchi(b)
			elif y == 3:
				giaitri() #Gọi hàm giaitri
				cuthenhapchi(c)
			else: break

	elif option == 2: #Bắt đầu Xuất
		xuat() #Gọi hàm xuat
		x = int(input("	Bạn muốn xuất dữ liệu nào? "))
		while x < 0 or x > 2:
			x = int(input("	Vui lòng nhập lại: "))
		if x == 1:
			nguon_chi() #Gọi hàm nguon_chi
			print('		4. Tổng số tiền đã chi')
			print('')
			y = int(input("	Bạn muốn xuất khoản chi tiêu nào? "))
			while y < 1 or y > 4:
				y = int(input("	Vui lòng nhập lại: "))
			if y == 1:
				canthiet() #Gọi hàm canthiet
				cuthexuat(a)
			elif y == 2:
				tietkiem() #Gọi hàm tietkiem
				cuthexuat(b)
			elif y == 3:
				giaitri() #Gọi hàm giaitri
				cuthexuat(c)
			elif y == 4:
				s = sum(a)+sum(b)+sum(c)
				print("	Tổng số tiền đã chi là: ",s ," VNĐ")
				print('	---------------------------------')
				tong = sum(t)
				print("	Lời khuyên chi tiêu: ")  #Đưa ra lời khuyên chi tiêu
				if ((sum(a)/tong) >= 0.47) and ((sum(a)/tong) <= 0.53) and ((sum(b)/tong) >= 0.17) and ((sum(b)/tong) <= 0.23) and ((sum(c)/tong) >= 0.27) and ((sum(c)/tong) <= 0.33):
					print("	Bạn có kế hoạch chi tiêu tuyệt vời! ^_^ ")
				else:
					if ((sum(a) / tong) > 0.53) and ((sum(c) / s) > 0.33) :
						print("	Bạn nên điều chỉnh lại kế hoạch chi tiêu bản thân và bớt ăn chơi đi! ~.~")
					elif ((sum(a) / tong) > 0.53) :
						print("	Bạn cần có kế hoạch chi tiêu tốt hơn! ~.~")
					elif ((sum(c) / tong) > 0.33):
						print("	Bạn cần bớt ăn xài lại! ~.~")
					else:
						print("	Bạn cần có kế hoạch chi tiêu tối ưu hơn!")
				time.sleep(2)
			else: break

		elif x == 2:
			print('	Thu nhập:')
			print('		Lương: ', t[0], ' VNĐ')
			print('		Thu nhập khác: ', t[1], ' VNĐ')
			tong = sum(a) + sum(b) + sum(c)
			du = sum(t) - tong
			print("	Đã chi: ", tong, " VNĐ")
			if du > 0:
				print('	---------------------------------')
				print("	Số tiền tiết kiệm được: ", du, " VNĐ")
				print('''
				Bạn có muốn cho vào quỹ đầu từ không?
					1. Có
					2. Không''')
				dautu = int(input('	Lựa chọn của bạn: '))
				while dautu < 1 or dautu > 2:
					dautu = int(input('	Vui lòng nhập lại: '))
				if dautu == 1:
					print('	---------------------------------')
					print("	Chúc mừng bạn đã có khoản đầu tư mới!")
					tiendautu = tiendautu + du  # Tiền dư sẽ chuyển thành tiền đã đầu tư
					b[0] = b[0] + du
					du = 0  # Tiền dư hết
					print("	Bạn đã đầu tư tổng cộng: ", tiendautu, " VNĐ")
				else:
					print('''
					Bạn chắc chứ?
						1. Không, tôi muốn đầu tư
						2. Tôi chắc chắn''')
					dautu = int(input('	Lựa chọn của bạn: '))
					while dautu < 1 or dautu > 2:
						dautu = int(input('	Vui lòng nhập lại: '))
					if dautu == 1:
						print('	---------------------------------')
						print("	Chúc mừng bạn đã có khoản đầu tư mới!")
						b[0] = b[0] + du
						tiendautu = tiendautu + du
						print("	Bạn đã đầu tư tổng cộng: ", tiendautu, " VNĐ")
					elif dautu == 2:
						print('''
	---------------------------------------------------------------------------
	|Giàu không tiết kiệm nghèo liền tay, nghèo không tiết kiệm sớm ăn mày !!!|
	---------------------------------------------------------------------------
						''')
					else: break
			elif du == 0:
				print('	---------------------------------')
				print('	Bạn đã hết tiền ~.~')
			elif du < 0:
				du = (-1) * du
				print('	---------------------------------')
				print("	Bạn đang nợ ", du, " VNĐ ~.~")
			else:
				break
			time.sleep(2)
	else:
		print("	Không có lựa chọn, hãy chọn lại!")

	print()
	time.sleep(2)
	clear()
	menu()
	option = int(input("	Bạn muốn nhập hay xuất dữ liệu? "))



