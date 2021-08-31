dict={"北京":{"昌平":{"沙河":{"起码路":{"羽绒教育园区":"狼腾测试员"}}}},
       "河北":{"邯郸":{"大名":{"大名府":{"卢府":"玉麒麟卢俊义"}}}}}
    # ,""
    #                                               河北":{"秦皇岛":{"北戴河":"海滨胜境"}}}

beijing=input("请输入您的地名")
if beijing=="北京":
    changping = input("请输入您的地名")
    if changping == "昌平":
        shahe = input("请输入您的地名")
        if shahe == "沙河":
            qml = input("请输入您的地名")
            if qml == "起码路":
                qyjyyq = input("请输入您的地名")
                if qyjyyq == "羽绒教育园区":
                    print(dict[beijing][changping][shahe][qml][qyjyyq])

else:
    print("判断错误，不是北京")
    handan = input("请输入您的地名")
    if handan == "邯郸":
        daming = input("请输入您的地名")
        if daming == "大名":
            damingfu = input("请输入您的地名")
            if damingfu == "大名府":
                lufu = input("请输入您的地名")
                if lufu == "卢府":
                    print(dict[beijing][handan][daming][damingfu][lufu])