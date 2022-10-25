# Pure Redux

## 바닐라 js를 이용한 todolist(by redux)

먼저 간단히 용어정리부터하자

1. createStore: state를 저장하는공간
2. action: state를 어떻게 바꿀지 객체형태로 reducer에 보내줌
3. reducer: store와 교류하는 함수로서 action의 객체를받고 state를 mutate한뒤 return해주는 역활
4. dispatch: action형태의 객체를 reducer로 전달하는 역활
5. subscribe: 기존의 redux에서는 state가 바뀌어도 바뀐것을 화면에 바로랜더링 해주지못해, subscribe를 통해 바뀐 state를 화면에 바꿔주는 역활을함

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />

    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />

    <title>Vanilla Redux</title>
  </head>
  <body>
    <form>
      <input/>
      <button>BTN</button>
    </form>
    <ul></ul>
</html>


```

이러한 형태의 html에서 redux를 이용해 state를 바꾸고, 화면에 출력

먼저 createStore를 설정해서 store를 설정해주고 reducer로 초기 state와 action 타입에따른 return할 state형태를 작성한다.

```
import { legacy_createStore } from "redux";

const form = document.querySelector("form");
const ul = document.querySelector("ul");
const input = document.querySelector("input");

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [...state, { text: action.text, id: Date.now() }];
    case DELETE_TODO:
      return state.filter((item) => item.id !== parseInt(action.id));
    default:
      return state;
  }
};

const store = legacy_createStore(reducer);

form.addEventListener("submit", onSubmit);
```

그다음 todolist의 input에 데이터를 추가하면 state에 값이 입력되고, 화면에 랜더링되는 코드를 작성해보자

```
const ADD_TODO = "ADD_TODO";

const addToDo = (text) => {
  return { type: ADD_TODO, text: text };
};

const dispatchaddTodo = (text) => {
  store.dispatch(addToDo(text));
};

const onSubmit = (e) => {
  e.preventDefault();
  const toDo = input.value;
  input.value = "";
  dispatchaddTodo(toDo);
};


// 변화후
const paintToDos = () => {
  // 앞의 중복을 없애기위해 작성
  ul.innerHTML = "";
  // 여기가중요
  const toDos = store.getState();
  toDos.forEach((toDo) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.addEventListener("click", dispatchdeleteTodo);
    li.id = toDo.id;
    li.innerText = toDo.text;
    btn.innerText = "DELETE";
    li.appendChild(btn);
    ul.appendChild(li);
  });
};
// 이걸해야 추가되든 삭제되는 결과값이 바뀐걸로 화면에 나옴
store.subscribe(paintToDos);

```

그다음 todolist에서 버튼을 통해 아이템을 제거하는 코드를 작성하자.

```
const DELETE_TODO = "DELETE_TOTO";

const deleteTodo = (id) => {
  return { type: DELETE_TODO, id: id };
};

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [...state, { text: action.text, id: Date.now() }];
    case DELETE_TODO:
      return state.filter((item) => item.id !== parseInt(action.id));
    default:
      return state;
  }
};

// 변화후
const paintToDos = () => {
  // 앞의 중복을 없애기위해 작성
  ul.innerHTML = "";
  // 여기가중요
  const toDos = store.getState();
  toDos.forEach((toDo) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.addEventListener("click", dispatchdeleteTodo);
    li.id = toDo.id;
    li.innerText = toDo.text;
    btn.innerText = "DELETE";
    li.appendChild(btn);
    ul.appendChild(li);
  });
};
// 이걸해야 추가되든 삭제되는 결과값이 바뀐걸로 화면에 나옴
store.subscribe(paintToDos);

```

정리해보면 특정 이벤트가 발생시 dispatch(action)을 통해 이벤트에 대해서 어떤식으로 state를 변화시킬지 reducer로 보내고,
reducer에서는 action에 해당하는 객체의 프로퍼티의 정보에따라 state를 바꿔서 return해주고 , 바뀐 state를 화면에 출력되도록 subscribe를 해주면된다
