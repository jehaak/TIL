```bash
npm i redux-saga
```



# 미들웨어를 사용해 Redux Store에 연결

```javascript
import { configureStore } from '@reduxjs/toolkit'
import createSagaMiddleware from 'redux-saga'

import reducer from './reducers'
import mySaga from './sagas'

// create the saga middleware
const sagaMiddleware = createSagaMiddleware()
// mount it on the Store
const store = configureStore(
  reducer, 
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(sagaMiddleware),
)

// then run the saga
sagaMiddleware.run(mySaga)
```





# 리듀서와 순수함수

- 리덕스는 state 객체의 주소값을 비교해서 변경을 감지한다
- 순수함수: 외부에 영향을 주지 않고, 외부 상태가 달라도 동일한 값을 받으면 동일한 값을 리턴함

- 순수함수 형태로 반환하면 새로운 주소값이 생성되 state의 변경을 항상 인지할 수 있다.
- 왜이렇게 만들어짐?
  - 주소값만 비교하면 바로 비교 가능
  - 주소는 같은데 내부 값까지 비교할려면 오래걸림



- 비동기 함수는 항상 같은 결과를 가져온다고 보장할 수 없기 때문에 리듀서안에서 사용할 수 없다.



- 이를 해결하기 위해 saga, thunk같은 미들웨어가 나옴
