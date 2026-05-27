while True:
    print("HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPEE")
    print(" 1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print(" 2. Chuẩn hóa tên shop")
    print(" 3. Kiểm tra mã giảm giá hợp lệ")
    print(" 4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print(" 5. Thoát chương trình")
    choise = input("Mời bạn chọn chức năng (1-5): ").strip()

    if not choise.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choise = int(choise)

    if choise < 1 or choise > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choise == 1:
        shop_name = input("Mời nhập tên shop: ").strip()
        if shop_name == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Mời nhập tên sản phẩm: ").strip()

        product_desc = input("Mời nhập mô tả sản phẩm: ").strip()
        if product_desc == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        product_cate = input("Mời nhập danh mục sản phẩm: ").strip()
        keywords_str = input("Mời nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ").strip()
        desc_leng = len(product_desc)
        
        cate_list = [c.strip().lower() for c in product_cate.split(" ") if c.strip() != ""]
        cate_normalized = " ".join(cate_list)

        kw_list = [k.strip() for k in keywords_str.split(",") if k.strip() != ""]
        kw_normalized = ", ".join(kw_list)
        kw_count = len(kw_list)

        print(f"Tên shop sau khi loại bỏ khoảng trắng đầu và cuối : {shop_name}")
        print(f"Tên sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ : {product_name.title()}")
        print(f"Mô tả sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối : {product_desc}")
        print(f"Độ dài mô tả sản phẩm : {desc_leng}")
        print(f"Danh mục sản phẩm sau khi chuẩn hóa khoảng trắng, chuyển hóa thành chữ thường : {cate_normalized}")
        print(f"Danh sách từ khóa sau khi chuẩn hóa khoảng trắng : {kw_normalized}")
        print(f"Số lượng từ khóa tìm kiếm : {kw_count}")
        print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ thường : {product_desc.lower()}")
        print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa : {product_desc.upper()}")

    elif choise == 2:
        if shop_name == "":
            print("Vui lòng chọn chức năng 1 để nhập thông tin trước")
            continue

        raw_shop = shop_name
        cleaned_shop = raw_shop.lower()
        
        words = [w for w in cleaned_shop.split(" ") if w != ""]
        connected_shop = "-".join(words)

        if connected_shop.startswith("shop-"):
            normalized_shop = connected_shop
        else:
            normalized_shop = "shop-" + connected_shop

        print(f"Tên shop ban đầu : {raw_shop}")
        print(f"Tên shop sau khi được chuẩn hóa : {normalized_shop}")

    elif choise == 3:
        code_check = input("Mời nhập một mã giảm giá để kiểm tra: ").strip()
        error_code = ""

        if len(code_check) == 0:
            error_code = "Mã giảm giá không được rỗng"
        elif " " in code_check:
            error_code = "Mã giảm giá không được chứa khoảng trắng"
        elif len(code_check) < 6 or len(code_check) > 12:
            error_code = "Mã giảm giá phải có độ dài từ 6 đến 12 ký tự"
        elif not code_check.isupper():
            error_code = "Mã giảm giá phải được viết hoa toàn bộ"
        elif not code_check.isalnum():
            error_code = "Mã giảm giá chỉ được chứa chữ cái và chữ số"
        elif not code_check.startswith("SALE"):
            error_code = "Mã giảm giá phải bắt đầu bằng chuỗi SALE"

        if error_code == "":
            print("Mã giảm giá hợp lệ")
            if keywords_str == "":
                keywords_str = code_check
            else:
                keywords_str += "," + code_check
            print(f"Danh sách mã giảm giá hiện tại: {keywords_str}")
        else:
            print(f"Mã giảm giá KHÔNG hợp lệ! Lý do: {error_code}")

    elif choise == 4:
        if product_desc == "":
            print("Vui lòng chọn chức năng 1 để nhập thông tin trước")
            continue

        search_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        if search_word in product_desc:
            app_word = product_desc.count(search_word)
            new_desc = product_desc.replace(search_word, replace_word)
            print(f"Số lần xuất hiện của từ khóa: {app_word}")
            print(f"Mô tả sau khi thay thế: {new_desc}")
            product_desc = new_desc
        else:
            print(f"Không tìm thấy từ khóa '{search_word}' trong mô tả sản phẩm.")

    elif choise == 5:
        print("Thoát chương trình")
        break