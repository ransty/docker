# Host: 16 cores, 64gb ram


## Docker settings: "userns-remap: default"

### fib(35), concurrency=6:

```
[2024-11-15 12:00:34,763: INFO/MainProcess] celery@64b4196dd6d2 ready.
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[cad6b7b4-8e7d-4efa-b855-348434ed177e] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[f40e4743-cf56-4b89-87a6-34a0bf85dcff] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[f10e6479-55e3-4d0a-846b-6d973e4799df] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[914acee6-07e9-45bc-b1a9-215221c58ce8] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[688bda91-a1a5-4004-9297-27c7a0b035f1] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[72e73f57-f569-4d07-b6a8-035a5fef9a23] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[a52b86b1-ff2a-45de-8955-9b258a534e86] received
[2024-11-15 12:00:34,764: INFO/MainProcess] Task app.fibonacci[eb4cd1f9-746b-4982-99ec-3a9976ef7569] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[ba7f4784-6c42-4edf-91d6-fcffc94f0db0] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[31f20a71-c60c-4c4b-9d6f-47813511f0c7] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[89ad636a-f3c8-4383-a77b-62c560062a1e] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[8401d7aa-e2f0-4728-875e-6daac878750a] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[a39f9a5e-c4e8-4df4-8469-7c2b17fe073d] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[d4c0bd00-2ef7-4368-8a98-6ef593617972] received
[2024-11-15 12:00:34,765: INFO/MainProcess] Task app.fibonacci[af23fc03-662e-4a03-ae9d-26039f16b0fc] received
[2024-11-15 12:04:01,339: INFO/ForkPoolWorker-4] Task app.fibonacci[cad6b7b4-8e7d-4efa-b855-348434ed177e] succeeded in 206.47252563999973s: 9227465
[2024-11-15 12:04:01,531: INFO/ForkPoolWorker-5] Task app.fibonacci[f10e6479-55e3-4d0a-846b-6d973e4799df] succeeded in 206.66501808700013s: 9227465
[2024-11-15 12:04:02,345: INFO/ForkPoolWorker-6] Task app.fibonacci[72e73f57-f569-4d07-b6a8-035a5fef9a23] succeeded in 207.47853643999952s: 9227465
[2024-11-15 12:04:02,493: INFO/ForkPoolWorker-1] Task app.fibonacci[f40e4743-cf56-4b89-87a6-34a0bf85dcff] succeeded in 207.62736567499996s: 9227465
[2024-11-15 12:04:02,981: INFO/ForkPoolWorker-2] Task app.fibonacci[914acee6-07e9-45bc-b1a9-215221c58ce8] succeeded in 208.11524868500055s: 9227465
[2024-11-15 12:04:03,124: INFO/ForkPoolWorker-3] Task app.fibonacci[688bda91-a1a5-4004-9297-27c7a0b035f1] succeeded in 208.2583151589988s: 9227465
[2024-11-15 12:07:28,805: INFO/ForkPoolWorker-4] Task app.fibonacci[a52b86b1-ff2a-45de-8955-9b258a534e86] succeeded in 207.46578546599994s: 9227465
[2024-11-15 12:07:28,855: INFO/ForkPoolWorker-5] Task app.fibonacci[eb4cd1f9-746b-4982-99ec-3a9976ef7569] succeeded in 207.32356695199996s: 9227465
[2024-11-15 12:07:29,967: INFO/ForkPoolWorker-6] Task app.fibonacci[ba7f4784-6c42-4edf-91d6-fcffc94f0db0] succeeded in 207.62166089199854s: 9227465
[2024-11-15 12:07:30,552: INFO/ForkPoolWorker-1] Task app.fibonacci[31f20a71-c60c-4c4b-9d6f-47813511f0c7] succeeded in 208.05847369099865s: 9227465
[2024-11-15 12:07:32,124: INFO/ForkPoolWorker-2] Task app.fibonacci[89ad636a-f3c8-4383-a77b-62c560062a1e] succeeded in 209.1419376319991s: 9227465
[2024-11-15 12:07:33,147: INFO/ForkPoolWorker-3] Task app.fibonacci[8401d7aa-e2f0-4728-875e-6daac878750a] succeeded in 210.02173839800162s: 9227465
[2024-11-15 12:10:48,635: INFO/ForkPoolWorker-5] Task app.fibonacci[d4c0bd00-2ef7-4368-8a98-6ef593617972] succeeded in 199.77951359100007s: 9227465
[2024-11-15 12:10:49,163: INFO/ForkPoolWorker-4] Task app.fibonacci[a39f9a5e-c4e8-4df4-8469-7c2b17fe073d] succeeded in 200.3571755440007s: 9227465
[2024-11-15 12:10:50,235: INFO/ForkPoolWorker-6] Task app.fibonacci[af23fc03-662e-4a03-ae9d-26039f16b0fc] succeeded in 200.26736944000004s: 9227465
```

**Total time:** 11 minutes
docker stats pinned CPU at 600%

### fib(35), concurrency=12:

```
[2024-11-15 12:12:50,708: INFO/MainProcess] celery@cf327041b5f5 ready.
[2024-11-15 12:12:50,708: INFO/MainProcess] Task app.fibonacci[cc353a94-3868-41ec-b245-6c1a7cc11131] received
[2024-11-15 12:12:50,708: INFO/MainProcess] Task app.fibonacci[9fad6d3b-7764-42ba-a28c-b560bd2bcce2] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[6738853e-70d7-4977-9563-7d4364a03b74] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[7f792951-cf63-4143-9221-26dbf0867032] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[2f221000-22f7-4a28-96a0-889d6f069f3b] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[56e5082d-5649-47d2-9535-db3338133e0c] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[c7acb19c-b667-47a6-8f45-cf0415fed8c1] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[0c57b1e0-ec53-4fc9-9b6d-21c49b03d347] received
[2024-11-15 12:12:50,709: INFO/MainProcess] Task app.fibonacci[7026d7f2-2710-4681-a7f1-673188535c13] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[7091f53f-8c87-4423-b570-5e067ef2c143] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[b057fc59-c6b6-4647-96e0-5fd0f0d3891b] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[97d3d198-46e5-46a0-b8d2-6c123b7f2e64] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[e5338ee7-7ab4-465a-be5d-ce1c4d2f9f49] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[39be63d3-0332-4578-98cd-7b0af461286e] received
[2024-11-15 12:12:50,710: INFO/MainProcess] Task app.fibonacci[1797d44f-72e8-4125-91cb-e12123160ebc] received
[2024-11-15 12:16:59,923: INFO/ForkPoolWorker-4] Task app.fibonacci[0c57b1e0-ec53-4fc9-9b6d-21c49b03d347] succeeded in 249.11216489899925s: 9227465
[2024-11-15 12:17:31,984: INFO/ForkPoolWorker-12] Task app.fibonacci[7026d7f2-2710-4681-a7f1-673188535c13] succeeded in 281.17261032999886s: 9227465
[2024-11-15 12:17:32,646: INFO/ForkPoolWorker-11] Task app.fibonacci[c7acb19c-b667-47a6-8f45-cf0415fed8c1] succeeded in 281.8349541810003s: 9227465
[2024-11-15 12:17:34,798: INFO/ForkPoolWorker-1] Task app.fibonacci[9fad6d3b-7764-42ba-a28c-b560bd2bcce2] succeeded in 283.9872817609994s: 9227465
[2024-11-15 12:17:52,626: INFO/ForkPoolWorker-5] Task app.fibonacci[7091f53f-8c87-4423-b570-5e067ef2c143] succeeded in 301.8150090470008s: 9227465
[2024-11-15 12:17:59,290: INFO/ForkPoolWorker-6] Task app.fibonacci[b057fc59-c6b6-4647-96e0-5fd0f0d3891b] succeeded in 308.4786964949999s: 9227465
[2024-11-15 12:18:03,943: INFO/ForkPoolWorker-10] Task app.fibonacci[2f221000-22f7-4a28-96a0-889d6f069f3b] succeeded in 313.1318105249993s: 9227465
[2024-11-15 12:18:04,413: INFO/ForkPoolWorker-3] Task app.fibonacci[56e5082d-5649-47d2-9535-db3338133e0c] succeeded in 313.60156875699977s: 9227465
[2024-11-15 12:18:08,491: INFO/ForkPoolWorker-7] Task app.fibonacci[97d3d198-46e5-46a0-b8d2-6c123b7f2e64] succeeded in 317.68021694399977s: 9227465
[2024-11-15 12:18:13,455: INFO/ForkPoolWorker-2] Task app.fibonacci[7f792951-cf63-4143-9221-26dbf0867032] succeeded in 322.644159159001s: 9227465
[2024-11-15 12:18:20,307: INFO/ForkPoolWorker-9] Task app.fibonacci[6738853e-70d7-4977-9563-7d4364a03b74] succeeded in 329.4963592570002s: 9227465
[2024-11-15 12:18:24,571: INFO/ForkPoolWorker-8] Task app.fibonacci[cc353a94-3868-41ec-b245-6c1a7cc11131] succeeded in 333.75985600499916s: 9227465
[2024-11-15 12:20:48,964: INFO/ForkPoolWorker-4] Task app.fibonacci[e5338ee7-7ab4-465a-be5d-ce1c4d2f9f49] succeeded in 229.0397513019998s: 9227465
[2024-11-15 12:21:10,012: INFO/ForkPoolWorker-12] Task app.fibonacci[39be63d3-0332-4578-98cd-7b0af461286e] succeeded in 218.02686364700094s: 9227465
[2024-11-15 12:21:10,207: INFO/ForkPoolWorker-11] Task app.fibonacci[1797d44f-72e8-4125-91cb-e12123160ebc] succeeded in 217.560012422s: 9227465
```

**Total time:** 9 minutes
docker stats pinned CPU at 1190%

<hr>

## Docker settings: "userns-remap: default", modified container CPU reservations


### fib(35), concurrency=6, cpu reserveration and limit of 6:

```
[2024-11-15 12:25:53,816: INFO/MainProcess] celery@e3795bdfe5d0 ready.
[2024-11-15 12:25:53,816: INFO/MainProcess] Task app.fibonacci[1051fd3e-de6b-4a18-a727-4370705a8362] received
[2024-11-15 12:25:53,816: INFO/MainProcess] Task app.fibonacci[1697b6e8-cca9-4f98-977e-e782d2926949] received
[2024-11-15 12:25:53,816: INFO/MainProcess] Task app.fibonacci[12e0671f-8e30-4262-b4ee-a230890cf37a] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[717ac3f4-64d2-448e-ba9b-2260045c60cc] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[14975634-7867-407f-95af-49c4fd9cedcc] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[d9f9e108-a8bd-465e-951c-8500bcf65701] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[e46f932f-0795-4d3a-a35a-94d435c0c2ec] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[08dcf8f1-3cef-4c8e-b16d-f2536b9ddca8] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[ad64a951-c9c2-4eaa-a803-744fc8e4d8eb] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[897e2620-8496-467e-afbc-c6e62481b913] received
[2024-11-15 12:25:53,817: INFO/MainProcess] Task app.fibonacci[65ea98a6-6e39-4695-8e8b-a2ad145dbba8] received
[2024-11-15 12:25:53,818: INFO/MainProcess] Task app.fibonacci[8103af06-7eeb-49b4-8270-5d7cbeadc489] received
[2024-11-15 12:25:53,818: INFO/MainProcess] Task app.fibonacci[cdb9ca17-16c3-4a4b-a272-1b6e7762811d] received
[2024-11-15 12:25:53,818: INFO/MainProcess] Task app.fibonacci[610cd3d2-151a-4b50-9130-e536e9b53391] received
[2024-11-15 12:25:53,818: INFO/MainProcess] Task app.fibonacci[17b4de6f-df5d-40e0-8075-ce6f71ca7f98] received
[2024-11-15 12:29:23,921: INFO/ForkPoolWorker-2] Task app.fibonacci[717ac3f4-64d2-448e-ba9b-2260045c60cc] succeeded in 210.00223370099957s: 9227465
[2024-11-15 12:29:23,978: INFO/ForkPoolWorker-6] Task app.fibonacci[d9f9e108-a8bd-465e-951c-8500bcf65701] succeeded in 210.05926541699955s: 9227465
[2024-11-15 12:29:24,719: INFO/ForkPoolWorker-3] Task app.fibonacci[14975634-7867-407f-95af-49c4fd9cedcc] succeeded in 210.79990173400074s: 9227465
[2024-11-15 12:29:24,753: INFO/ForkPoolWorker-1] Task app.fibonacci[1697b6e8-cca9-4f98-977e-e782d2926949] succeeded in 210.83463363900046s: 9227465
[2024-11-15 12:29:24,833: INFO/ForkPoolWorker-4] Task app.fibonacci[1051fd3e-de6b-4a18-a727-4370705a8362] succeeded in 210.9147621209995s: 9227465
[2024-11-15 12:29:25,953: INFO/ForkPoolWorker-5] Task app.fibonacci[12e0671f-8e30-4262-b4ee-a230890cf37a] succeeded in 212.03399458200147s: 9227465
[2024-11-15 12:32:55,797: INFO/ForkPoolWorker-6] Task app.fibonacci[08dcf8f1-3cef-4c8e-b16d-f2536b9ddca8] succeeded in 211.81891323699892s: 9227465
[2024-11-15 12:32:56,854: INFO/ForkPoolWorker-2] Task app.fibonacci[e46f932f-0795-4d3a-a35a-94d435c0c2ec] succeeded in 212.93256698999903s: 9227465
[2024-11-15 12:32:56,982: INFO/ForkPoolWorker-4] Task app.fibonacci[65ea98a6-6e39-4695-8e8b-a2ad145dbba8] succeeded in 212.14818233500046s: 9227465
[2024-11-15 12:32:57,029: INFO/ForkPoolWorker-3] Task app.fibonacci[ad64a951-c9c2-4eaa-a803-744fc8e4d8eb] succeeded in 212.3102512179994s: 9227465
[2024-11-15 12:32:58,269: INFO/ForkPoolWorker-1] Task app.fibonacci[897e2620-8496-467e-afbc-c6e62481b913] succeeded in 213.51480605799952s: 9227465
[2024-11-15 12:32:59,137: INFO/ForkPoolWorker-5] Task app.fibonacci[8103af06-7eeb-49b4-8270-5d7cbeadc489] succeeded in 213.18408555500173s: 9227465
[2024-11-15 12:36:20,236: INFO/ForkPoolWorker-6] Task app.fibonacci[cdb9ca17-16c3-4a4b-a272-1b6e7762811d] succeeded in 204.43784087399945s: 9227465
[2024-11-15 12:36:20,876: INFO/ForkPoolWorker-2] Task app.fibonacci[610cd3d2-151a-4b50-9130-e536e9b53391] succeeded in 204.02138223600014s: 9227465
[2024-11-15 12:36:21,341: INFO/ForkPoolWorker-4] Task app.fibonacci[17b4de6f-df5d-40e0-8075-ce6f71ca7f98] succeeded in 204.3583231470002s: 9227465
```

**Total time:** 11 minutes
docker stats pinned CPU at 600%


### fib(35), concurrency=12, cpu reservation and limit of 12:

```
[2024-11-15 12:37:06,584: INFO/MainProcess] celery@37fe2963f0f8 ready.
[2024-11-15 12:37:06,584: INFO/MainProcess] Task app.fibonacci[f460c371-2a3f-4ea1-ada7-4853f8961d02] received
[2024-11-15 12:37:06,584: INFO/MainProcess] Task app.fibonacci[3955a25b-fa47-4ffc-95a3-3d6b478e8524] received
[2024-11-15 12:37:06,584: INFO/MainProcess] Task app.fibonacci[95746e18-f3cd-4bb8-b8b8-fbfcfbfe50d4] received
[2024-11-15 12:37:06,584: INFO/MainProcess] Task app.fibonacci[44123048-d3e5-4c22-979e-748d5cfe7748] received
[2024-11-15 12:37:06,584: INFO/MainProcess] Task app.fibonacci[12261baf-f08c-4b75-8ac9-29dfccce765e] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[8731d26f-484d-4a91-b73a-c3646fcb1300] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[fff06c19-42b1-45f8-9c11-a47cf1019e6c] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[dbf3d3ce-c989-46a3-ad05-2fa0ef583bff] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[6c6baa35-fe17-409e-87a0-a2f63b13782f] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[b8f9274a-3ebb-4e93-8e63-fbcfeb13b437] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[b84cea2a-763a-4973-bd37-e0fafc6c39ee] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[29af6c00-2f08-432f-96dd-212d97cf8fb2] received
[2024-11-15 12:37:06,585: INFO/MainProcess] Task app.fibonacci[c7687bf3-d673-48fb-bec4-6386f8814c08] received
[2024-11-15 12:37:06,586: INFO/MainProcess] Task app.fibonacci[db27c83d-8ac7-4ec4-9cc9-ee881f0d3520] received
[2024-11-15 12:37:06,586: INFO/MainProcess] Task app.fibonacci[9a6807ac-1bcd-40c7-9647-e367622e4e43] received
[2024-11-15 12:41:23,060: INFO/ForkPoolWorker-5] Task app.fibonacci[b8f9274a-3ebb-4e93-8e63-fbcfeb13b437] succeeded in 256.37283668499913s: 9227465
[2024-11-15 12:41:30,806: INFO/ForkPoolWorker-3] Task app.fibonacci[8731d26f-484d-4a91-b73a-c3646fcb1300] succeeded in 264.11931539500074s: 9227465
[2024-11-15 12:42:02,144: INFO/ForkPoolWorker-10] Task app.fibonacci[12261baf-f08c-4b75-8ac9-29dfccce765e] succeeded in 295.45672221600034s: 9227465
[2024-11-15 12:42:02,958: INFO/ForkPoolWorker-9] Task app.fibonacci[95746e18-f3cd-4bb8-b8b8-fbfcfbfe50d4] succeeded in 296.27118613700077s: 9227465
[2024-11-15 12:42:22,663: INFO/ForkPoolWorker-7] Task app.fibonacci[29af6c00-2f08-432f-96dd-212d97cf8fb2] succeeded in 315.97583841099913s: 9227465
[2024-11-15 12:42:22,715: INFO/ForkPoolWorker-1] Task app.fibonacci[3955a25b-fa47-4ffc-95a3-3d6b478e8524] succeeded in 316.02819416700004s: 9227465
[2024-11-15 12:42:29,337: INFO/ForkPoolWorker-8] Task app.fibonacci[f460c371-2a3f-4ea1-ada7-4853f8961d02] succeeded in 322.65045030500005s: 9227465
[2024-11-15 12:42:30,726: INFO/ForkPoolWorker-4] Task app.fibonacci[dbf3d3ce-c989-46a3-ad05-2fa0ef583bff] succeeded in 324.0388217539985s: 9227465
[2024-11-15 12:42:35,327: INFO/ForkPoolWorker-6] Task app.fibonacci[b84cea2a-763a-4973-bd37-e0fafc6c39ee] succeeded in 328.6399985199987s: 9227465
[2024-11-15 12:42:39,612: INFO/ForkPoolWorker-11] Task app.fibonacci[fff06c19-42b1-45f8-9c11-a47cf1019e6c] succeeded in 332.925399533s: 9227465
[2024-11-15 12:42:40,883: INFO/ForkPoolWorker-12] Task app.fibonacci[6c6baa35-fe17-409e-87a0-a2f63b13782f] succeeded in 334.1962224220006s: 9227465
[2024-11-15 12:42:46,553: INFO/ForkPoolWorker-2] Task app.fibonacci[44123048-d3e5-4c22-979e-748d5cfe7748] succeeded in 339.86652367900024s: 9227465
[2024-11-15 12:45:06,834: INFO/ForkPoolWorker-3] Task app.fibonacci[db27c83d-8ac7-4ec4-9cc9-ee881f0d3520] succeeded in 216.02754213200024s: 9227465
[2024-11-15 12:45:20,166: INFO/ForkPoolWorker-5] Task app.fibonacci[c7687bf3-d673-48fb-bec4-6386f8814c08] succeeded in 237.10529744700034s: 9227465
[2024-11-15 12:45:40,464: INFO/ForkPoolWorker-10] Task app.fibonacci[9a6807ac-1bcd-40c7-9647-e367622e4e43] succeeded in 218.31974321300004s: 9227465
```

**Total time:** 8 minutes
docker stats pinned CPU at 1200%


### Notes
This was to test if Docker is limiting resourcing despite celery reporting the correct amount of threads for prefork pool
