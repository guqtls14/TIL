# Definitely Typed

## d.ts란?

- 자바스크립트 생태계에있는 npm packages는 항상 types을 갖고있는 환경이아님
- 때로는 프로젝트가 더 이상 유지 관리되지 않고 다른 경우에는 TypeScript를 쓸지안쓸지 확실히 알수없음.

## Using non-typed NPM packages in TypeScript

- 위와같은 문제를 해결하기위해 Definitely typed을 주자
- Definely Type은 유형이 없는 NPM 패키지에 대한 TypeScript 정의의 중앙 저장소를 제공하는 프로젝트임.

```
npm install --save-dev @types/jquery
```

이런식으로 설치함!

- 패키지를 설치한 후 유형을 사용하기 위해 뭘 더해줄건없음. 패키지 자체를 사용할 때 TypeScript가 자동으로 유형을 선택함.

### 참고

[w3cDT설명](https://www.w3schools.com/typescript/typescript_definitely_typed.php)
[stackoverflow설명](https://stackoverflow.com/questions/50463990/what-are-d-ts-files-for)
