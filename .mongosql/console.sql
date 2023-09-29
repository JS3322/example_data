//CREATE
db.createCollection("test100", {})

//READ
db.test100.countDocuments()

use test

function  getRandomInt(max) {
    return Math.floor(Math.random() * Math.random(max))
}

for (let i = 0; i < 50000; i++) {
    let doc = {
        name: "user" + getRandomInt(10000),
        age: getRandomInt(100)
    };
    db.test100.insertOne(doc);
}

print("All documents inserted");


//CREATE
db.createCollection(
    "TB_INDEX_TEST1",                           /* <-- 컬렉션 이름 */
    {
        timeseries: {                     /* <-- Timeseries 컬렉션임을 정의 */
            timeField: "timestamp",        /* <-- 시간이 들어가는 필드명 지정 */
            metaField: "metadata",         /* <-- 메타 데이터 필드명 지정 */
            granularity: "hours"           /* <-- granularity 설정(옵션) */
        },
        expireAfterSeconds: 604800        /* <-- TTL 인덱스 사용가능 */
    }
)