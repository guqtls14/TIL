# HTML이란?

- html은 마크업 언어로서 웹 브라우저에게 웹페이지가 어떤식으로 구조화 되있는지 알려주는 역활을 한다.

1. [html구성요소](#html-구성요소)

   1. [nesting elements](#nesting-elements)
   2. [block & inline](#block-vs-inline-elements)
   3. [void](#void-elements)

2. [attributes](#attributes)
   1. [boolean attributes](#boolean-attributes)
3. [html 구조](#html-document-구조)
   1. [기호](#entity-references-including-special-characters-in-html)

## html 구성요소

![해부도](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started/grumpy-cat-small.png)

html요소는 오픈태크,컨텐트,클로우즈테크의 형식으로 만들어짐

### nesting elements

```
<p>My Cat is <strong>very</strong> grupmy!</p>

```

&lt;strong&gt; 처럼 태그안에 쌓인 태그를 nesting elements라고함

### Block vs Inline elements

html에는 block level elements와 inline level elements로 나뉨

1. block elements
   - 블록 엘레먼츠는 앞선 컨텐츠의 다음줄에 나타나는 특징이있음.
   - 블록 레벨 요소는 일반적으로 페이지의 구조 요소임.
     - 예를들어 블록요소는 headings,paragraphs,lists,navigation menus or footer등을 의미함
   - 블록 요소는 인라인 요소의 내부 엘레먼츠로 들어갈수는 없음
   - 하지만 다른 블록요소의 내부에는 nesting 가능!
2. inline elements
   - 인라인 요소는 블록 요소안에 포함되며, documents's content의 일부 작은 부분임
   - 인라인 요소는 새로운 홈페이지에서 새로운 Line을 형성하지는 않음
   - 예를들어 text,a태그,hyperlink,em,strong등이 예시임

### void elements

- 쉽게말해 오픈태그와 닫힌태그의 형식이아닌 start tag만있는 태그를 얘기함

```
<img
  src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png" alt="Firefox icon" />

```

이런 식으로 작성됨

## attributes

- elements는 속성을 갖는데 다음과 같이 나타남

![속성이미지](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started/grumpy-cat-attribute-small.png)

- attributes는 element에 관한 다수의 정보를 갖고있는데 content로 나타나는 정보는 아님
- 예를들어 **class** attribut는 스타일 정보로 요소를 대상으로 하는 데 사용되는 식별 이름입니다.

### Boolean attributes

- 떄때로 우리는 값이없이 작성된 attributes를 볼수있음

- 이러한 속성은 Boolean attributes라고함

- Boolean attributes는 일반적으로 속성 이름과 동일한 값을 하나만 가질 수 있습니다.

```
<input type="text" disabled="disabled" />

```

## HTML document 구조

- html document는 다음과 같이 구조화 되어있다.

```
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>

```

1. **&lt;!DOCTYPE html&gt;**

   - doctype은 HTML 페이지가 좋은 HTML로 간주되기 위해 따라야 하는 일련의 규칙에 대한 링크 역할을 하도록 의도되음

2. **&lt;html>&lt;/html&gt;**

- html element로서 모든 page의 content를 둘러싸고있음
- 때때로 root element라고도 불림

3. **&lt;head>&lt;/head&gt;**
   - html 페이지에서 포함되어있는 모든것을 담은 컨테이너 역활을함
   - 페이지의 **content** 를 보여주는 역활은아님(사용자에게 표시할 내용을 담지는않음)
   - keyword,페이지설명,검색결과등의 내용을 담으며 css style content등과같은 정보를 담고있음
4. **&lt;meta charset="utf-8"&gt;**

   - meta원소로서 meta데이터를 담고있음
   - charset attributes는 쉽게말해 문서에 대한 문자 집합을 UTF-8로 설정. 이 문자 집합에는 대부분의 사람이 쓰는 언어의 문자가 포함. 이 설정을 사용하면 페이지는 포함할 수 있는 모든 텍스트 내용을 처리할 수 있음. 이 설정을 하지 않을 이유가 없으며, 나중에 문제가 발생하지 않도록 하는 데 도움이 될 수 있음.
     - [utf-8설명](https://meaningone.tistory.com/191)
     - [부호화](https://itpenote.tistory.com/361)

5. **&lt;title>&lt;/title&gt;>**

   - page의 title을 설정

6. **&lt;body>&lt;/body&gt;**

   - 화면에 표시되는 모든 content가 담겨있는 태그

### Entity references: Including special characters in HTML

- html에서 >,<,"",&등은 특별한 문자임
- 만일 위의 기호를 쓰려면 다음과 같이해야함

![기호이미지](./img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-10-20%20%EC%98%A4%ED%9B%84%202.41.49.png)

예시로서

```
<p>In HTML, you define a paragraph using the <p> element.</p>

<p>In HTML, you define a paragraph using the &lt;p&gt; element.</p>

```

위와 같은 코드가있음
