## getter,setter

### 인덱싱

- [getter&setter](#getter--setter)
- [getter](#getter)
- [setter](#setter)
- [사용예시](#사용예시)
- [참고](#참고)

  객체의 프로퍼티는 크게 2가지로 나뉨

1. 데이터프로퍼티로써 지금까지 사용한 모든 프로퍼티는 데이터 프로퍼티임

2. 접근자 프로퍼티라 불리는 새로운 프로퍼티임
   - 접근자 프로퍼티의 본질은 함수인데, 이 하수는 값을 획득(get)하고 설정(set)하는 역활을함.
   - 외부에서 볼때는 일반적인 프로퍼티처럼 보임

### getter & setter

- 접근자 프로퍼티는 'getter(획득자)'와 ‘setter(설정자)’ 메서드로 표현됩니다. 객체 리터럴 안에서 getter와 setter 메서드는 get과 set으로 나타낼 수 있습니다.

```
let obj = {
  get propName() {
    // getter, obj.propName을 실행할 때 실행되는 코드
  },

  set propName(value) {
    // setter, obj.propName = value를 실행할 때 실행되는 코드
  }
};

```

getter메서드는 obj.propName을 사용해 프로퍼티를 읽으려할때 실행,
setter메서드는 obj.propName=value으로 프로퍼티에 값을 할당하려할때 실행

### getter

```
let user = {
  name: "John",
  surname: "Smith",

  get fullName() {
    return `${this.name} ${this.surname}`;
  }
};

alert(user.fullName); // John Smith
```

- 접근자 프로퍼티를 사용하면 함수처럼 호출하지않고, 일반 프로퍼티에서 값에 접근하는것처럼 평범하게
  user.fullName을 사용해서 프로퍼티 값을 얻을수있음

- 나머지 작업은 getter 메서드가 뒷단에서 처리

하지만 만약 위 예시에서 fullName은 getter메서드만 있기에 user.fullName= 을 사용해 값을 할당하면 에러임!

```
"use strict";

let user = {
  get fullName() {
    return `...`;
  }
};

user.fullName = "Test"; // Error (프로퍼티에 getter 메서드만 있어서
```

### setter

```
let user = {
  name: "John",
  surname: "Smith",

  get fullName() {
    return `${this.name} ${this.surname}`;
  },

  set fullName(value) {
    [this.name, this.surname] = value.split(" ");
  }
};

// 주어진 값을 사용해 set fullName이 실행됩니다.
user.fullName = "Alice Cooper";

alert(user.name); // Alice
alert(user.surname); // Cooper
```

다음과 같이 setter메서드를 할당해서 오류가 안뜨고 제대로 할당됨을 알수있음

```
let a = {
  get lalala() {
    this._live1 += 10;
    return this._live1;
  },

  set lalala(value) {
    if (typeof value === "string") {
      alert("No String!!");
    } else {
      this._live1 = value;
    }
  },
};

a.lalala = "string"; // string이라고 alert가뜸
// alert(a.lalala);

a.lalala = 123;
alert(a.lalala); // 133
```

그외 이러한 예시들이있음

### 사용예시

```
class User {
  constructor(firstname, lastname, age) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
  }

  get age() {
    // getter, User.age를 실행할 때 실행되는 코드
    this._age = this._age + 1;
    return this._age;
  }

  set age(value) {
    // setter, User.age = value 를 실행할 때 실행되는 코드
    if (value < 0) {
      throw Error("age can not be negative");
    }
    this._age = value;
  }
}

const user1 = new User("Steve", "Job", 15);

console.log("1", user1.age);
console.log("2", user1.age);
console.log("3", user1.age);
const user2 = new User("Steve", "Job", -15);

console.log(user2.age);

```

객체지향에서 위와같이 사용가능!

### 참고

> [사용이유](https://axce.tistory.com/m/59)

> [모던자바스크립트설명](https://ko.javascript.info/property-accessors)

> [class예시](https://axce.tistory.com/m/59)
