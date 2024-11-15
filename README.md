# Docker settings: None

## fib(35), concurrency=1

```
celery-1  | [2024-11-15 10:27:16,614: INFO/MainProcess] celery@48c0217e69fc ready.
celery-1  | [2024-11-15 10:27:16,614: INFO/MainProcess] Task app.fibonacci[75692d4f-e6d9-48b5-b254-3eb827443bc1] received
celery-1  | [2024-11-15 10:30:33,691: INFO/ForkPoolWorker-1] Task app.fibonacci[75692d4f-e6d9-48b5-b254-3eb827443bc1] succeeded in 196.97579250000035s: 9227465
celery-1  | Task result: 9227465
```

## fib(35), concurrency=4

```
celery-1  | [2024-11-15 10:37:17,281: INFO/MainProcess] celery@4c29f9e22432 ready.
celery-1  | [2024-11-15 10:37:17,281: INFO/MainProcess] Task app.fibonacci[e74d54b8-f788-4bd6-b1bd-56db0b90ce45] received
celery-1  | [2024-11-15 10:40:25,813: INFO/ForkPoolWorker-2] Task app.fibonacci[e74d54b8-f788-4bd6-b1bd-56db0b90ce45] succeeded in 188.43086198399942s: 9227465
celery-1  | Task result: 9227465
```


# Docker settings: userns-remap: default

## fib(35), concurrency=1

```
celery-1  | [2024-11-15 10:43:47,260: INFO/MainProcess] celery@0d2b83d100d1 ready.
celery-1  | [2024-11-15 10:43:47,261: INFO/MainProcess] Task app.fibonacci[527af6b5-64ad-460a-8387-598a1ef6a1bd] received
celery-1  | [2024-11-15 10:46:59,683: INFO/ForkPoolWorker-2] Task app.fibonacci[527af6b5-64ad-460a-8387-598a1ef6a1bd] succeeded in 192.32152322599995s: 9227465
celery-1  | Task result: 9227465
```

## fib(35), concurrency=4

```

```

# Docker settings: userns-remap: default, nofile: 100,200, nproc:1024,2048
## fib(35), concurrency=1

```

```

## fib(35), concurrency=4

```

```

# Docker settings: userns-remap: default, nofile: 100,200, nproc:1024,2048,


### Notes
Cores kept swapping between C3, C4, C11 & C12 on my host

16 cores, 64gb ram
