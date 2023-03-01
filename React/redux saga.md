- 리덕스만 쓰면 힘들어서 리덕스 툴킷도 써야된다

```bash
npm i redux-saga
npm install @reduxjs/toolkit
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

- 외부상태에 영향을 받지 않고(같은 인풋값에 대해 항상 같은 아웃풋을 내는 것), 또 외부 상태를 바꾸지 않는 함수가 순수함수
- 리덕스는 이전값과 이후 값의 비교를 통해 값의 변화를 인지한다.
  - Redux의 State는 불변해야 한다는 특징을 가지고 있습니다. 불변한다는 것은 state가 변경되면 안된다는 뜻이 아니라 state가 수정되면 안된다는 뜻 입니다.

