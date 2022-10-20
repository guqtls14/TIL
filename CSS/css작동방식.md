## css작동방식

1. [css작동](#css는-어떻게-작동됨)

2. [DOM정보](#dom정보)

3. [실제DOM적용](#실제-dom-표현)

4. [DOMcss적용](#dom에-css적용)

### css는 어떻게 작동됨?

- 브라우저가 문서를 표시할때, 문서의 콘텐츠와 해당 스타일 정보를 결합해야함.

- 결합은 다음과 같은 순서로 작동

  - 1. 브라우저는 HTML(예를들어 네트워크에서 html을 수신)을 로드
  - 2. HTML을 DOM으로 변환. DOM은 컴퓨터 메모리의 문서를 나타냄
  - 3. 브라우저는 html안에있는 이미지 및 비디오와 같은 정보와 연결된 css를 가져옴. js는 나중에처리
  - 4. 브라우저는 가져온 css를 분석하고 선택자 유형별로 정리(요소,class,id등 파싱된 css 정보를 기반으로 dom의 어느 노드에 어떤 규칙을 적용해야 하는지 결정하고, 필요에 따라 스타일을 첨부함(이 단계를 render tree라고함))
  - 5. render tree는 규칙이 적용된 후에 표시되야하는 구조로 배치됨
  - 6. 페이지의 시각적 표시가 화면에 표시(이 단계를 painting이라고함)

### DOM정보

- DOM은 트리와 같은 구조를 가지고있음
- html 마크업 언어의 각 요소,속성 및 텍스트는 트리구조에서 DOM node가 됨
- 노드는 다른 DOM 노드와의 관계에 의해 정의됨
- 일부 요소는 자식 노드의 부모이고, 자식 노드에는 형제가 있음
- DOM은 css와 문서의 내용이 만나는 곳이기에 DOM을이용하면 css설계및 디버그관리에 좋음

### 실제 DOM 표현

```
<p>
  Let's use:
  <span>Cascading</span>
  <span>Style</span>
  <span>Sheets</span>
</p>

```

위의 코드에서 p태그는 부모노드이고 자식은 텍스트노드이면서 span요소에 해당하는 세개의 노드는 p의 자식노드임

```
P
├─ "Let's use:"
├─ SPAN
|  └─ "Cascading"
├─ SPAN
|  └─ "Style"
└─ SPAN
   └─ "Sheets"

```

다음과 같이 구조화됨

### DOM에 css적용

- 만일 css를 문서에 추가하여 스타일을 지정했다면 다음과같은 과정이 진행됨

```
span {
  border: 1px solid black;
  background-color: lime;
}

```

- 브라우저는 html을 구문분석하고 그다음 dom을 작성한 다음, css를 구문 분석을함
- css에서 span에 관한 css적용이있으므로 브라우저는 css구문분석을해 적용을함

css까지 적용을 하면 다음과같은 결과가나옴
![css결과](./img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-10-20%20%EC%98%A4%ED%9B%84%203.23.03.png)
