import streamlit as st
# 터미널에서 스트림릿 실행시키는 문구
# streamlit run streamlit/test.py(실행하고자 하는 폴더/파일)

# 화면 상단
st.markdown('# 띵동 🎀')
st.markdown('## 깜짝 선물이 도착했습니다!')
st.markdown('### 2023/10/23 Mon')

# 사이드 바
with st.sidebar:
    st.header('🐲❤️🐯')

# 사이드바-토글(체크 누르면 오디오가 나오게-경환아 화이팅!)
add_toggle = st.sidebar.toggle('❤️❤️❤️')

if add_toggle:
    st.sidebar.caption('소리가 조금 클수도 있어!으ㅏㅏ아 부끄럽다,,')
    st.sidebar.audio('streamlit\Fighting.m4a')
    
# 사이드바-슬라이더(만족도)
point = st.sidebar.slider('', 0, 100)
st.sidebar.write("내 생각에,", point, '점이야')


# 탭(편지 내용, 응원 문구)
tab1, tab2 = st.tabs(["Cheer up", "Remind"])

with tab1:
    st.text("크하하 놀랐지?")
    st.text('머신러닝, 딥러닝 수업이 끝나고 오늘부턴 새로운걸 배우고 있어')
    st.text('파이썬 코드로 웹사이트를 만드는건데\n배운걸로 경환이 웃게 해주고 싶어서 또 실습 겸 만들어봤지!')
    st.text('안그래도 연초에 코딩 처음 배울때, 이런 사이트 만들어서 짠! 하고 보여달라고 했었잖아.'
            '\n이번에 배우길래 생각났어 ㅎㅎ 부족하지만 힘이 좀 나려나?!')
    st.text('하나씩 배울때마다 경환이한테 어떻게 보여줄까? 하는 생각에 신나!!'
            '\n혜린이 머리속에 연관검색어 1위로 올라와 있는 소감이 어떠신가요?ㅋㅋ')
    st.text('처음하는거라 코드 자체가 익숙하진 않은데 재밌어')
    st.text('그래서 드는 생각인데 경환이가 정말 열심히 노력해서 편입하는 만큼!!'
            '\n서울로 상경하는거 자체도 목표이긴 하겠지만,, 이왕이면 흥미가 있는 학과에 꼭 붙으면 좋겠어!'
            '\n내가 느끼기에 재미가 없으면 결국엔 졸업장만 남는거 같아'
            '\n공부하면서도 경환이 스스로를 돌아보면서 좋아하는건 뭘까? 하고싶은건 뭘까? 하는 고민도 추천해~')
    st.text('나는 경환이가 응원해준 덕분에?! 새로운 흥미를 찾아서 취준을 준비하게 되서 굉장히 뜻깊어!👍'
            '\n경환이도 나한테서 좋은 영향만 가득가득 받아가~')
    st.text('경환아 보고싶어❤️'
            '\n아자아자 화이팅!')
    st.caption('디자인 실력도, 글 솜씨도 양해 부탁해,,ㅋㅋㅋㅋㅋㅋ')
        

with tab2:
    st.text('나는 할 수 있다!')
    st.text('나는 잘 하고 있다!')
    st.text('한양대에 찰떡같이 붙을거다!')
    st.text('경환이는 한양대 건축학과 학생이다!!')
    st.text('꿈을 이룰거다!')
    st.text('1년 동안의 노력이 빛을 발할거다!')
    st.subheader('멋지다 이경환!')
    st.caption("매일 다짐하는거야!")
    st.image('streamlit\picture2.jpg')