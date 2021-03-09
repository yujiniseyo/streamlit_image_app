#에자일 방식 : 돌아가는 코드 만들어놓고 살을 붙이면서 작업
import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import os
from datetime import datetime

# 디렉토리와 이미지을 주면, 해당 디렉토리에 이 이미지을 저장하는 함수
def save_uploaded_file(directory, img) :
    
    #  1. 디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    
    #  2. 디렉토리가 있으니까, 이미지 저장
    filename = datetime.now().isoformat().replace(':','-').replace('.','-')
    img.save(directory+'/'+filename+'.jpg')
    return st.success('Saved img : {} in {}'.format(filename+'.jpg', directory))


def load_image(image_file) :
    img = Image.open(image_file)
    return img


def main() :

    image_file_list = st.file_uploader('Upload Image' , type = ['png' , 'jpg' , 'jpeg'] , accept_multiple_files = True)

    print(image_file_list)

    if image_file_list is not None :

        # 2. 각 파일을 이미지로 바꿔줌
        image_list = []

        # 2-1. 모든 파일이 image_list에 이미지로 저장됨
        for image_file in image_file_list :
            img = load_image(image_file)
            image_list.append(img)

        # # 3. 이미지를 화면에 확인해봄 (디버깅용)
        # for img in image_list :
        #     st.image(img)

        option_list = ['Show Image' , 'Rotate Image' , 'Create Thumbnail' , 'Crop Image' , 'Merge Images' , 'Flip Image' , 'Change Color' , 'Filters - Sharpen' , 'Filters - Edge Enhance' , 'Contrast Image']
        option = st.selectbox('옵션을 선택하세요.' , option_list)



        if option == 'Show Image' :

            origin_img_list = []
            for img in image_list :
                st.image(img)
                origin_img_list.append(img)

            directory = st.text_input('폴더명을 입력해주세요')

            if st.button('SAVE') :

                for img in origin_img_list :
                    save_uploaded_file(directory, img)


        elif option == 'Rotate Image' :

            # 1. 유저가 입력
            degree = st.number_input('각도 입력', 0, 360)

            # 2. 모든 이미지 회전
            transformed_img_list = []
            for img in image_list :
                rotated_img = img.rotate(degree)
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)
            
            # 3. 디렉토리 입력받음
            directory = st.text_input('폴더명을 입력해주세요')

            # 4. save 버튼 만들기
            if st.button('SAVE') :
                
                # 5. 파일 저장 코드
                for img in transformed_img_list :
                    save_uploaded_file(directory, img)



        elif option == 'Create Thumbnail' :
            # 1. 이미지 사이즈

            width = st.number_input('width 입력', 1, 100)
            height = st.number_input('height 입력', 1, 100)

            size = (width, height)

            transformed_img_list = []
            for img in image_list :
                img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)

            directory = st.text_input('폴더명을 입력해주세요')

            if st.button('SAVE') :

                for img in transformed_img_list :
                    save_uploaded_file(directory, img)



        # elif option == 'Crop Image' :
        #     # 시작좌표 + (너비,높이) => 크롭 종료 좌표
            
        #     start_x = st.number_input('시작 X 좌표 입력', 0, img.size[0] - 1)
        #     start_y = st.number_input('시작 Y 좌표 입력', 0, img.size[1] - 1)
            
        #     # 예외처리
        #     max_width = img.size[0] - start_x
        #     max_height = img.size[1] - start_y
            
        #     width = st.number_input('width 입력', 1, max_width)
        #     height = st.number_input('height 입력', 1, max_height)

        #     box = (start_x, start_y, start_x + width, start_y + height)
        #     st.write(box)
        #     croppped_img = img.crop(box)
        #     croppped_img.save('data/crop.png')
        #     st.image(croppped_img)



        # elif option == 'Merge Images' :

        #     merge_file = st.file_uploader('Upload Image' , type = ['png' , 'jpg' , 'jpeg'] , key = 'merge')

        #     if merge_file is not None :

        #         merge_img = load_image(merge_file)

        #         start_x = st.number_input('시작 X 좌표 입력', 0, img.size[0] - 1)
        #         start_y = st.number_input('시작 Y 좌표 입력', 0, img.size[1] - 1)

        #         position = (start_x, start_y)

        #         img.paste(merge_img, position)

        #         st.image(img)



        elif option == 'Flip Image' :
            status = st.radio('플립 선택', ['FLIP_LEFT_RIGHT' , 'FLIP_TOP_BOTTOM'])
    
            if status == 'FLIP_LEFT_RIGHT' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
    
            elif status == 'FLIP_TOP_BOTTOM' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
                    
            directory = st.text_input('폴더명을 입력해주세요')

            if st.button('SAVE') :

                for img in transformed_img_list :
                    save_uploaded_file(directory, img)



        # elif option == 'Change Color' :
        #     # img.convert('L')에서 L은 그레이스케일, 1은 흑백
        #     status = st.radio('색상 선택', [ 'Color', 'Gray Scale' ,'Black & White' ] , key = 'color')
    
        #     if status == 'Color' :
        #         color = 'RGB'
    
        #     elif status == 'Gray Scale' :
        #         color = 'L'

        #     elif status == 'Black & White' :
        #         color = '1'

        #     bw = img.convert(color)
        #     st.image(bw)



        # elif option == 'Filters - Sharpen' :
        #     sharp_img = img.filter(ImageFilter.SHARPEN) # 선명하게
        #     st.image(sharp_img)



        # elif option == 'Filters - Edge Enhance' :
        #     edge_img = img.filter(ImageFilter.EDGE_ENHANCE) # 선이 진하고 두껍게 (윤곽선 강조?)
        #     st.image(edge_img)



        # elif option == 'Contrast Image' :
        #     contrast_img = ImageEnhance.Contrast(img).enhance(2)
        #     st.image(contrast_img)
            




if __name__ == '__main__' :
    main()