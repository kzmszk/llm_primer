## markdown extension 使い方

### Preview
* view preview: command + k v
* file import: @import "file name"
* ダイヤグラム: mermaid or kurokiが使える
* プレゼン: [公式ドキュメント](https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/presentation)

### All in one
* create table: "Create Table of Content" in command pallet

### mermaid サンプル
```mermaid
sequenceDiagram
Alice->>John: Hello John, how are you?
loop HealthCheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!
```

```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```
