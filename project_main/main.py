# 用户界面
print("\t欢迎使用购物车管理系统！")
print("\n")
print("##########购物车系统##########")
print("#        1.添加购物车        #")
print("#        2.修改购物车        #")
print("#        3.删除购物车        #")
print("#        4.查询购物车        #")
print("#        5.退出购物车        #")
print("##############_##############")
print()
shopping_cart = dict()
# 选择数据结构为：shopping_cart = {"Meta80": {"price": 6999, "num": 2},"鼠标": {"price": 99, "num": 1}}
# 因为将商品名称设计为key就可以满足需求了
while True:
    score = input("请选择要执行的操作：（输入1-5）：")
    match score:
        case "1":#添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"商品价格":goods_price,"商品数量":goods_num}
                print("商品已添加成功")
        case "2":#修改购物车
            goods_name = input("请输入要修改的商品名称：")
            goods_price = float(input("请输入要修改的商品价格："))
            goods_num = int(input("请输入要修改的商品数量："))

            if goods_name not in shopping_cart:
                print("该商品不存在，请先前往录入信息")
            else:
                shopping_cart[goods_name] = {"商品价格":goods_price,"商品数量":goods_num}
                print("商品信息已修改")
        case "3":#删除购物车
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请先前往录入信息")
            else:
                del shopping_cart[goods_name]
                print("商品已删除")
        case "4":#查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info['商品价格']},商品数量：{goods_info['商品数量']}")
        case "5":
            print()
            print("系统已退出")
            break
        case _: #匹配其他所有情况只需要写下划线
            print("请输入正确的内容（非法操作）")




