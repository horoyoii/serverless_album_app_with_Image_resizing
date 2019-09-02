# serverless_album_app_with_Image_resizing
FaaS를 통한 서버리스 앨범 앱 with 이미지 리사이징
<br/><br/><br/>
## Contents
- [시나리오](#시나리오)
- [데모영상](#데모영상)
- [스크린샷](#스크린샷)
- [How to Implement](#How_to_Implement)

<br/><br/><br/>

## 시나리오

![Untitled Diagram (3)](https://user-images.githubusercontent.com/34915108/64122222-f0067e00-cddb-11e9-84c3-cddd63100f71.png)

 1. aws s3는 관련 javascirpt sdk를 제공하여 브라우저에서 직접 파일을 업로드할 수 있게 해준다.
이 때 aws cognito를 활용하여 안전하게 s3 버킷에 접근할 수 있다.
 2. 이를 통해 브라우저에서  파일을 업로드하게 되면 s3에 파일에 저장되는데 
s3와 aws lamdba를 연결시켜 "s3에 파일이 업로드되었음!" 라는 이벤트를 lambda 함수가 받게 된다.
 3. 이후 이미지 처리 라이브러리인 pillow를 활용하는 python 함수가 트리거되어 원본 이미지를 리사이징하여 
s3에 다시 저장하는 작업을 수행한다. 

<br/><br/><br/>
## 데모영상
[Youtube link](https://www.youtube.com/watch?v=XmVl7ZWWMXs)


<br/><br/><br/>
## 스크린샷

### 1.클라이언트에서 origin 폴더에 이미지를 업로드할 수 있다.
![1](https://user-images.githubusercontent.com/34915108/64122379-6c00c600-cddc-11e9-9c70-5aab8d0adfdb.PNG)


### 2.이 이미지는 s3에 업로드되고 결과를 브라우저에서 확인 가능하다.
![2](https://user-images.githubusercontent.com/34915108/64122386-73c06a80-cddc-11e9-9a3d-fd70c976dae1.PNG)

### 3. w2, w4, w6 폴더에 들어가면 각각 정의된 작은 크기로 리사이즈된 썸네일 이미지가 생성되고 이를 다운로드 받을 수 있다.
![3](https://user-images.githubusercontent.com/34915108/64122404-7e7aff80-cddc-11e9-8cb1-c67a5a802aa5.PNG)


<br/><br/><br/>

## How to Implement

### 1.aws IAM을 통한 aws lambda와 aws s3 연결 방법
[aws IAM을 통한 aws lambda와 s3 연결 방법](https://blog.naver.com/demonic3540/221635831475)

### 2. aws lambda에 zip형태의 함수 등록

 1. CreateThumbnail.zip 파일을 아래의 업로드 버튼을 통해 등록.
 2. CreateThumbnail.py 에서 s3 접근 후 이미지 리사이징 및 다시 저장 기능이 구현되어있음. 
![image](https://user-images.githubusercontent.com/34915108/64122855-b6cf0d80-cddd-11e9-8ebd-189b674508f1.png)
