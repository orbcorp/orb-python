# Changelog

## 1.39.1 (2024-01-18)

Full Changelog: [v1.39.0...v1.39.1](https://github.com/orbcorp/orb-python/compare/v1.39.0...v1.39.1)

### Bug Fixes

* **ci:** ignore stainless-app edits to release PR title ([#146](https://github.com/orbcorp/orb-python/issues/146)) ([5a2e2b5](https://github.com/orbcorp/orb-python/commit/5a2e2b58b7763a99907ae3a3a8afd6a19789cb62))


### Chores

* **internal:** fix typing util function ([#140](https://github.com/orbcorp/orb-python/issues/140)) ([31a83a9](https://github.com/orbcorp/orb-python/commit/31a83a9d24ba25004ab234dc1b555a03d7333a1f))
* **internal:** remove redundant client test ([#142](https://github.com/orbcorp/orb-python/issues/142)) ([e315f4e](https://github.com/orbcorp/orb-python/commit/e315f4e00c4e2a45a657d56df3a22813264632a3))
* **internal:** share client instances between all tests ([#145](https://github.com/orbcorp/orb-python/issues/145)) ([64a4cb6](https://github.com/orbcorp/orb-python/commit/64a4cb6dfc3b5947701dba25dbe8c37b6050eb38))
* **internal:** speculative retry-after-ms support ([#143](https://github.com/orbcorp/orb-python/issues/143)) ([d7affe9](https://github.com/orbcorp/orb-python/commit/d7affe9e3fae951027d43307df10420143e69042))
* lazy load raw resource class properties ([#144](https://github.com/orbcorp/orb-python/issues/144)) ([72734a3](https://github.com/orbcorp/orb-python/commit/72734a340d158aae1e039d615a72bff2b9d89454))

## 1.39.0 (2024-01-17)

Full Changelog: [v1.38.1...v1.39.0](https://github.com/orbcorp/orb-python/compare/v1.38.1...v1.39.0)

### Features

* **api:** updates ([#139](https://github.com/orbcorp/orb-python/issues/139)) ([ab7998f](https://github.com/orbcorp/orb-python/commit/ab7998fa311038357c124fe556b9cd1a664d826b))


### Chores

* add write_to_file binary helper method ([#138](https://github.com/orbcorp/orb-python/issues/138)) ([f48014d](https://github.com/orbcorp/orb-python/commit/f48014d0792e01dde7206088ab672c6012d00deb))
* **internal:** updates to proxy helper ([#136](https://github.com/orbcorp/orb-python/issues/136)) ([15d29d5](https://github.com/orbcorp/orb-python/commit/15d29d513cd6b58fee06b6165bc2ce16fba7e096))

## 1.38.1 (2024-01-16)

Full Changelog: [v1.38.0...v1.38.1](https://github.com/orbcorp/orb-python/compare/v1.38.0...v1.38.1)

### Bug Fixes

* **client:** ensure path params are non-empty ([#134](https://github.com/orbcorp/orb-python/issues/134)) ([f318392](https://github.com/orbcorp/orb-python/commit/f318392b5ff32e4b53a021773220fda59aae0920))

## 1.38.0 (2024-01-15)

Full Changelog: [v1.37.0...v1.38.0](https://github.com/orbcorp/orb-python/compare/v1.37.0...v1.38.0)

### Features

* **api:** updates ([#133](https://github.com/orbcorp/orb-python/issues/133)) ([ace1234](https://github.com/orbcorp/orb-python/commit/ace12344fddc86150429c497f64f7fca030fc24e))
* **client:** add support for streaming raw responses ([#132](https://github.com/orbcorp/orb-python/issues/132)) ([171a504](https://github.com/orbcorp/orb-python/commit/171a504c2c74724fbedcd82d3696e8e1acf18eb9))


### Chores

* formatting ([#130](https://github.com/orbcorp/orb-python/issues/130)) ([4ae6c11](https://github.com/orbcorp/orb-python/commit/4ae6c1177b9d67e82baa44c4560e1372bfbd2f0a))

## 1.37.0 (2024-01-12)

Full Changelog: [v1.36.0...v1.37.0](https://github.com/orbcorp/orb-python/compare/v1.36.0...v1.37.0)

### Features

* add `None` default value to nullable response properties ([#123](https://github.com/orbcorp/orb-python/issues/123)) ([823f95c](https://github.com/orbcorp/orb-python/commit/823f95c2b504524de1bc65e00ca088d2552fad7b))
* **api:** add beta evaluate price endpoint ([#129](https://github.com/orbcorp/orb-python/issues/129)) ([5f8379a](https://github.com/orbcorp/orb-python/commit/5f8379a3acea6a9937219cb6878991a05a8c50b4))


### Chores

* add .keep files for examples and custom code directories ([#126](https://github.com/orbcorp/orb-python/issues/126)) ([672693d](https://github.com/orbcorp/orb-python/commit/672693d7c7cfec8d55d54ab328ea4c89f3527b55))
* **client:** improve debug logging for failed requests ([#127](https://github.com/orbcorp/orb-python/issues/127)) ([b35adf9](https://github.com/orbcorp/orb-python/commit/b35adf9795ce2321640904d43eb4ff806c8a1af8))
* **internal:** loosen type var restrictions ([#125](https://github.com/orbcorp/orb-python/issues/125)) ([60a2816](https://github.com/orbcorp/orb-python/commit/60a28169d5912c1a76f128c02012c062f507cb1f))
* **internal:** replace isort with ruff ([#121](https://github.com/orbcorp/orb-python/issues/121)) ([42b60df](https://github.com/orbcorp/orb-python/commit/42b60dfa929e6806fbddf6138af4df5a1557f2d7))
* use property declarations for resource members ([#124](https://github.com/orbcorp/orb-python/issues/124)) ([b60f5a8](https://github.com/orbcorp/orb-python/commit/b60f5a8a44687083c627d284fe3f7c105a3bbb84))


### Documentation

* **readme:** improve api reference ([#128](https://github.com/orbcorp/orb-python/issues/128)) ([5fbd017](https://github.com/orbcorp/orb-python/commit/5fbd01703a0dd0dd90f7359a703a8d6693c608ca))

## 1.36.0 (2024-01-01)

Full Changelog: [v1.35.2...v1.36.0](https://github.com/orbcorp/orb-python/compare/v1.35.2...v1.36.0)

### Features

* **api:** add currency fields ([#119](https://github.com/orbcorp/orb-python/issues/119)) ([35574d3](https://github.com/orbcorp/orb-python/commit/35574d339cff2ed011a17433af556ffed02af9b7))

## 1.35.2 (2023-12-28)

Full Changelog: [v1.35.1...v1.35.2](https://github.com/orbcorp/orb-python/compare/v1.35.1...v1.35.2)

### Bug Fixes

* **client:** correctly use custom http client auth ([#117](https://github.com/orbcorp/orb-python/issues/117)) ([863ebe8](https://github.com/orbcorp/orb-python/commit/863ebe87f4881f01afa7a39286a5b154ca047305))

## 1.35.1 (2023-12-26)

Full Changelog: [v1.35.0...v1.35.1](https://github.com/orbcorp/orb-python/compare/v1.35.0...v1.35.1)

### Bug Fixes

* use brackets instead of commas for array query params ([#116](https://github.com/orbcorp/orb-python/issues/116)) ([a03afeb](https://github.com/orbcorp/orb-python/commit/a03afeb4c13765e905a3e5fc8e52e1da4fa8e4be))


### Chores

* **ci:** run release workflow once per day ([#107](https://github.com/orbcorp/orb-python/issues/107)) ([8399dca](https://github.com/orbcorp/orb-python/commit/8399dcad701cac68076d88efba8aa2f6d456ad4b))
* **internal:** add bin script ([#113](https://github.com/orbcorp/orb-python/issues/113)) ([ed19a63](https://github.com/orbcorp/orb-python/commit/ed19a63151d3f4119fa70b68459242030a4ba199))
* **internal:** fix typos ([#111](https://github.com/orbcorp/orb-python/issues/111)) ([e2ba1db](https://github.com/orbcorp/orb-python/commit/e2ba1db59f6d8e86c625310d5017ece279788bd2))
* **internal:** minor utils restructuring ([#110](https://github.com/orbcorp/orb-python/issues/110)) ([1946480](https://github.com/orbcorp/orb-python/commit/19464809e1a6d4ba122b767ed59551ec0509503e))
* **internal:** updates to base client ([#108](https://github.com/orbcorp/orb-python/issues/108)) ([53ea238](https://github.com/orbcorp/orb-python/commit/53ea2380bb8280bd679255afed4300daeb1620ea))
* **internal:** use ruff instead of black for formatting ([#115](https://github.com/orbcorp/orb-python/issues/115)) ([ed83783](https://github.com/orbcorp/orb-python/commit/ed837839d28c1191bb4656577b8d80a411ce82dd))
* **package:** bump minimum typing-extensions to 4.7 ([#112](https://github.com/orbcorp/orb-python/issues/112)) ([440c756](https://github.com/orbcorp/orb-python/commit/440c756ffab480330f7a01dbbb129a26f41c1612))


### Documentation

* **api:** updates ([#109](https://github.com/orbcorp/orb-python/issues/109)) ([692c3e8](https://github.com/orbcorp/orb-python/commit/692c3e8ea49d3fe7dfc2f03d78be25cc2237fb9f))
* avoid normalizing trailing space ([#106](https://github.com/orbcorp/orb-python/issues/106)) ([09fd3f8](https://github.com/orbcorp/orb-python/commit/09fd3f8e37d3138bd32532aba6729e24b208684c))
* improve README timeout comment ([#101](https://github.com/orbcorp/orb-python/issues/101)) ([69a6970](https://github.com/orbcorp/orb-python/commit/69a6970e11ba88969a3c17dcd4374f8197b88dca))


### Refactors

* **client:** simplify cleanup ([#103](https://github.com/orbcorp/orb-python/issues/103)) ([54ac0dd](https://github.com/orbcorp/orb-python/commit/54ac0ddb1b703e011e84f184e6e90ee9f31e2055))
* remove unused model types used in params ([#105](https://github.com/orbcorp/orb-python/issues/105)) ([e18a59e](https://github.com/orbcorp/orb-python/commit/e18a59e47125aafb2e81f29f45fe9e866c738d28))
* simplify internal error handling ([#104](https://github.com/orbcorp/orb-python/issues/104)) ([cd0f847](https://github.com/orbcorp/orb-python/commit/cd0f8472457ac651c2fa44dc1e464cac78257c59))

## 1.35.0 (2023-12-11)

Full Changelog: [v1.34.1...v1.35.0](https://github.com/orbcorp/orb-python/compare/v1.34.1...v1.35.0)

### Features

* **api:** updates ([#99](https://github.com/orbcorp/orb-python/issues/99)) ([3b9bc05](https://github.com/orbcorp/orb-python/commit/3b9bc053aab713661aa372952e44e30a76f8bd81))

## 1.34.1 (2023-12-08)

Full Changelog: [v1.34.0...v1.34.1](https://github.com/orbcorp/orb-python/compare/v1.34.0...v1.34.1)

### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#97](https://github.com/orbcorp/orb-python/issues/97)) ([b65cdf2](https://github.com/orbcorp/orb-python/commit/b65cdf2017fa80622e879ad6c4c700cbe04fb329))

## 1.34.0 (2023-12-08)

Full Changelog: [v1.33.4...v1.34.0](https://github.com/orbcorp/orb-python/compare/v1.33.4...v1.34.0)

### Features

* **api:** remove unsupported field ([#95](https://github.com/orbcorp/orb-python/issues/95)) ([fbb9a6a](https://github.com/orbcorp/orb-python/commit/fbb9a6ad26b452fbf8985007f770ed2c903e3b66))

## 1.33.4 (2023-12-08)

Full Changelog: [v1.33.3...v1.33.4](https://github.com/orbcorp/orb-python/compare/v1.33.3...v1.33.4)

### Bug Fixes

* **errors:** properly assign APIError.body ([#94](https://github.com/orbcorp/orb-python/issues/94)) ([7ee4eea](https://github.com/orbcorp/orb-python/commit/7ee4eea7f164e0b0685149d1591571c6c9566d77))


### Chores

* **internal:** enable more lint rules ([#93](https://github.com/orbcorp/orb-python/issues/93)) ([a3dd337](https://github.com/orbcorp/orb-python/commit/a3dd3377f5246ba6d1302224981a45c9c3a9121d))
* **internal:** minor updates to pagination ([#91](https://github.com/orbcorp/orb-python/issues/91)) ([cc341f4](https://github.com/orbcorp/orb-python/commit/cc341f40366a81e9f1db9bd4ad049d2228cc15b5))
* **internal:** reformat imports ([#89](https://github.com/orbcorp/orb-python/issues/89)) ([26a17d4](https://github.com/orbcorp/orb-python/commit/26a17d4cd116a58ce16657bc8e189bbd4dda775a))
* **internal:** reformat imports ([#92](https://github.com/orbcorp/orb-python/issues/92)) ([55b46bb](https://github.com/orbcorp/orb-python/commit/55b46bb375aee8a00d79177bad06c907d854b1fa))
* **internal:** update formatting ([#90](https://github.com/orbcorp/orb-python/issues/90)) ([ce98611](https://github.com/orbcorp/orb-python/commit/ce98611dd7fe75931d01f7119244388c51224a74))

## 1.33.3 (2023-12-04)

Full Changelog: [v1.33.2...v1.33.3](https://github.com/orbcorp/orb-python/compare/v1.33.2...v1.33.3)

### Chores

* **package:** lift anyio v4 restriction ([#84](https://github.com/orbcorp/orb-python/issues/84)) ([70cbb10](https://github.com/orbcorp/orb-python/commit/70cbb104fe927cebfa5e3d42a3c29f0ed4ab19ab))

## 1.33.2 (2023-12-01)

Full Changelog: [v1.33.1...v1.33.2](https://github.com/orbcorp/orb-python/compare/v1.33.1...v1.33.2)

### Bug Fixes

* **client:** correct base_url setter implementation ([#83](https://github.com/orbcorp/orb-python/issues/83)) ([83ad98c](https://github.com/orbcorp/orb-python/commit/83ad98c68e6103792d0e9739db105c82ae44f6f4))


### Chores

* **internal:** remove unused type var ([#82](https://github.com/orbcorp/orb-python/issues/82)) ([a9a3dbe](https://github.com/orbcorp/orb-python/commit/a9a3dbe325cbc0b3621469208871a616abe3979b))
* **internal:** replace string concatenation with f-strings ([#81](https://github.com/orbcorp/orb-python/issues/81)) ([d290faf](https://github.com/orbcorp/orb-python/commit/d290faf226356c4968bca7308306ae02e6bcb600))


### Documentation

* **readme:** update example snippets ([#79](https://github.com/orbcorp/orb-python/issues/79)) ([da58b27](https://github.com/orbcorp/orb-python/commit/da58b276e4c352f5f1bacb03455277f33f872243))

## 1.33.1 (2023-11-30)

Full Changelog: [v1.33.0...v1.33.1](https://github.com/orbcorp/orb-python/compare/v1.33.0...v1.33.1)

### Bug Fixes

* **client:** ensure retried requests are closed ([#78](https://github.com/orbcorp/orb-python/issues/78)) ([af69dbb](https://github.com/orbcorp/orb-python/commit/af69dbbf926375b4383badf61b22471ccca48661))


### Chores

* **internal:** add tests for proxy change ([#77](https://github.com/orbcorp/orb-python/issues/77)) ([3d80ca9](https://github.com/orbcorp/orb-python/commit/3d80ca9ba3dcadafe21c2066b7e605c27771edf9))
* **internal:** update lock file ([#74](https://github.com/orbcorp/orb-python/issues/74)) ([d3c1761](https://github.com/orbcorp/orb-python/commit/d3c1761a169d423394d0ae6a7f30a0549d344029))
* **internal:** updates to proxy helper ([#76](https://github.com/orbcorp/orb-python/issues/76)) ([80e0f3d](https://github.com/orbcorp/orb-python/commit/80e0f3dc784b29adc1b32005f5bfc75f51fff2e3))

## 1.33.0 (2023-11-28)

Full Changelog: [v1.32.0...v1.33.0](https://github.com/orbcorp/orb-python/compare/v1.32.0...v1.33.0)

### Features

* **api:** updates ([#73](https://github.com/orbcorp/orb-python/issues/73)) ([1e4d614](https://github.com/orbcorp/orb-python/commit/1e4d6148fcb859c095fd46e21841aff004475430))


### Chores

* **deps:** bump mypy to v1.7.1 ([#72](https://github.com/orbcorp/orb-python/issues/72)) ([e7f7b47](https://github.com/orbcorp/orb-python/commit/e7f7b47e99c4e1ae73c09de6c83d8879e0172bae))
* **internal:** options updates ([#67](https://github.com/orbcorp/orb-python/issues/67)) ([8f91e55](https://github.com/orbcorp/orb-python/commit/8f91e55e750372c77dfd98202cd445560343e747))
* **internal:** revert recent options change ([#70](https://github.com/orbcorp/orb-python/issues/70)) ([6ff55a6](https://github.com/orbcorp/orb-python/commit/6ff55a6bff7f7281b6288cb7a3042fd51e3a29f0))
* **internal:** send more detailed x-stainless headers ([#71](https://github.com/orbcorp/orb-python/issues/71)) ([7dd46f3](https://github.com/orbcorp/orb-python/commit/7dd46f3ed8ba12999cbb3376b48f01c12f7e80e3))


### Documentation

* **api:** update metadata docstrings ([#69](https://github.com/orbcorp/orb-python/issues/69)) ([cf25b7c](https://github.com/orbcorp/orb-python/commit/cf25b7c8280a5dae5796fc5506db794ccba3b425))

## 1.32.0 (2023-11-22)

Full Changelog: [v1.31.2...v1.32.0](https://github.com/orbcorp/orb-python/compare/v1.31.2...v1.32.0)

### Features

* **api:** updates ([#66](https://github.com/orbcorp/orb-python/issues/66)) ([cfefc76](https://github.com/orbcorp/orb-python/commit/cfefc763c7d1e08e280b076ee5c88274ab42c1a4))


### Chores

* **client:** improve copy method ([#63](https://github.com/orbcorp/orb-python/issues/63)) ([ae3eed5](https://github.com/orbcorp/orb-python/commit/ae3eed56e988ff66e793116c8a0c80c5b5d87869))
* **package:** add license classifier metadata ([#65](https://github.com/orbcorp/orb-python/issues/65)) ([da28530](https://github.com/orbcorp/orb-python/commit/da28530b636f74e64a343957437daaeb80da49ef))

## 1.31.2 (2023-11-21)

Full Changelog: [v1.31.1...v1.31.2](https://github.com/orbcorp/orb-python/compare/v1.31.1...v1.31.2)

### Bug Fixes

* **client:** attempt to parse unknown json content types ([#61](https://github.com/orbcorp/orb-python/issues/61)) ([2ff1f69](https://github.com/orbcorp/orb-python/commit/2ff1f69a8a7b6a138002cf8eef49d76e71a6bb2e))

## 1.31.1 (2023-11-20)

Full Changelog: [v1.31.0...v1.31.1](https://github.com/orbcorp/orb-python/compare/v1.31.0...v1.31.1)

### Chores

* **internal:** update some test values ([#60](https://github.com/orbcorp/orb-python/issues/60)) ([cf1e4a9](https://github.com/orbcorp/orb-python/commit/cf1e4a9a241eb6fdd66f42f05f5dbaa2c3fec2ed))
* **internal:** update type hint for helper function ([#59](https://github.com/orbcorp/orb-python/issues/59)) ([191e197](https://github.com/orbcorp/orb-python/commit/191e19734a80480dfaa4ea614baef2d565264bea))


### Documentation

* **readme:** fix link to docs website ([#58](https://github.com/orbcorp/orb-python/issues/58)) ([4510e87](https://github.com/orbcorp/orb-python/commit/4510e8728e7282b16c9e91ca97b74106681b0666))
* **readme:** minor updates ([#56](https://github.com/orbcorp/orb-python/issues/56)) ([0d09713](https://github.com/orbcorp/orb-python/commit/0d097132f1884d193e8fee9a781c29d8afe25f32))

## 1.31.0 (2023-11-16)

Full Changelog: [v1.30.3...v1.31.0](https://github.com/orbcorp/orb-python/compare/v1.30.3...v1.31.0)

### Features

* **api:** updates ([#55](https://github.com/orbcorp/orb-python/issues/55)) ([dbfb455](https://github.com/orbcorp/orb-python/commit/dbfb455e7019597b33f723b9d5682e378489eb2d))
* **client:** support reading the base url from an env variable ([#54](https://github.com/orbcorp/orb-python/issues/54)) ([04d5ca5](https://github.com/orbcorp/orb-python/commit/04d5ca523c38a36e72c42587e323a55b7a9d09a4))


### Chores

* **internal:** fix devcontainer interpeter path ([#52](https://github.com/orbcorp/orb-python/issues/52)) ([a35fe95](https://github.com/orbcorp/orb-python/commit/a35fe959fe9bbe9a4ecd4a50148c4c5d447643b6))
* **internal:** fix typo in NotGiven docstring ([#50](https://github.com/orbcorp/orb-python/issues/50)) ([7e1d704](https://github.com/orbcorp/orb-python/commit/7e1d704c9a4baebf09bb9b95d4e0baf5e2c9809e))


### Documentation

* fix code comment typo ([#53](https://github.com/orbcorp/orb-python/issues/53)) ([0171b18](https://github.com/orbcorp/orb-python/commit/0171b183ee377d4c1aaa9dab7d0c4faaa1b1c1f9))

## 1.30.3 (2023-11-13)

Full Changelog: [v1.30.2...v1.30.3](https://github.com/orbcorp/orb-python/compare/v1.30.2...v1.30.3)

### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#48](https://github.com/orbcorp/orb-python/issues/48)) ([52d5c13](https://github.com/orbcorp/orb-python/commit/52d5c134035252e12290930ffc7797f3e386f7cc))

## 1.30.2 (2023-11-10)

Full Changelog: [v1.30.1...v1.30.2](https://github.com/orbcorp/orb-python/compare/v1.30.1...v1.30.2)

### Bug Fixes

* **client:** serialise pydantic v1 default fields correctly in params ([#46](https://github.com/orbcorp/orb-python/issues/46)) ([dc058e3](https://github.com/orbcorp/orb-python/commit/dc058e30be77833522880b651a7eed16b23bc7c3))

## 1.30.1 (2023-11-10)

Full Changelog: [v1.30.0...v1.30.1](https://github.com/orbcorp/orb-python/compare/v1.30.0...v1.30.1)

### Bug Fixes

* **models:** mark unknown fields as set in pydantic v1 ([#45](https://github.com/orbcorp/orb-python/issues/45)) ([c965317](https://github.com/orbcorp/orb-python/commit/c9653177220c301b99b95455a58c0cdd9088091e))


### Chores

* **internal:** base client updates ([#44](https://github.com/orbcorp/orb-python/issues/44)) ([79ff165](https://github.com/orbcorp/orb-python/commit/79ff1652c90c689452ed7e2ce264f72ae9c1bfe5))


### Documentation

* reword package description ([#42](https://github.com/orbcorp/orb-python/issues/42)) ([6994f49](https://github.com/orbcorp/orb-python/commit/6994f492fe7c0e890017bf0275990cc5a0ae147e))

## 1.30.0 (2023-11-09)

Full Changelog: [v1.29.0...v1.30.0](https://github.com/orbcorp/orb-python/compare/v1.29.0...v1.30.0)

### Features

* **api:** updates ([#41](https://github.com/orbcorp/orb-python/issues/41)) ([ea5d1a4](https://github.com/orbcorp/orb-python/commit/ea5d1a460b0c2ee26ed2844b3f19cbc65762b922))
* **client:** support passing chunk size for binary responses ([#40](https://github.com/orbcorp/orb-python/issues/40)) ([6cc1be0](https://github.com/orbcorp/orb-python/commit/6cc1be01b788208d963cd8c4a300ca8c8649420d))
* **client:** support passing httpx.Timeout to method timeout argument ([#35](https://github.com/orbcorp/orb-python/issues/35)) ([65c7fc9](https://github.com/orbcorp/orb-python/commit/65c7fc93f25d8d651f6dcb0472a98695d6d4acb6))


### Chores

* **docs:** fix github links ([#38](https://github.com/orbcorp/orb-python/issues/38)) ([2a83f73](https://github.com/orbcorp/orb-python/commit/2a83f73006fb0edbc063360b90bad706375ca318))
* **internal:** fix some typos ([#37](https://github.com/orbcorp/orb-python/issues/37)) ([b0fc909](https://github.com/orbcorp/orb-python/commit/b0fc909f70c539d529b1eeb24aa4aa9683999dbd))
* **internal:** improve github devcontainer setup ([#39](https://github.com/orbcorp/orb-python/issues/39)) ([3fabb8f](https://github.com/orbcorp/orb-python/commit/3fabb8f4bc47f418b7d4ec7833048589802298db))

## 1.29.0 (2023-11-06)

Full Changelog: [v1.28.1...v1.29.0](https://github.com/orbcorp/orb-python/compare/v1.28.1...v1.29.0)

### Features

* **api:** remove unsupported params ([#33](https://github.com/orbcorp/orb-python/issues/33)) ([abd325f](https://github.com/orbcorp/orb-python/commit/abd325f78c1d58c30207bf69ba36b32229626fac))

## 1.28.1 (2023-11-06)

Full Changelog: [v1.28.0...v1.28.1](https://github.com/orbcorp/orb-python/compare/v1.28.0...v1.28.1)

### Bug Fixes

* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#32](https://github.com/orbcorp/orb-python/issues/32)) ([f21abfa](https://github.com/orbcorp/orb-python/commit/f21abfae14e1897cd501e09a1dc3051e5c7e54ec))


### Chores

* **internal:** remove unused int/float conversion ([#29](https://github.com/orbcorp/orb-python/issues/29)) ([0b701e1](https://github.com/orbcorp/orb-python/commit/0b701e1812c7293fd313f759944e400e202eab69))


### Documentation

* **readme:** improve example snippets ([#31](https://github.com/orbcorp/orb-python/issues/31)) ([3815aad](https://github.com/orbcorp/orb-python/commit/3815aad75faa9ce55a499eaabb04c3c3f15b1701))

## 1.28.0 (2023-11-03)

Full Changelog: [v1.27.0...v1.28.0](https://github.com/orbcorp/orb-python/compare/v1.27.0...v1.28.0)

### Features

* **api:** updates ([#13](https://github.com/orbcorp/orb-python/issues/13)) ([4256067](https://github.com/orbcorp/orb-python/commit/42560678cd0b5bdfeafb5f3940aa06e6266fc193))
* **api:** updates ([#8](https://github.com/orbcorp/orb-python/issues/8)) ([c9c4a66](https://github.com/orbcorp/orb-python/commit/c9c4a664b617f2e6749ccecdd83580adf3ff8a33))
* **client:** adjust retry behavior to be exponential backoff ([#4](https://github.com/orbcorp/orb-python/issues/4)) ([62c25f6](https://github.com/orbcorp/orb-python/commit/62c25f6cf9456cb3ea26a79272417e79b366603c))
* **client:** allow binary returns ([#26](https://github.com/orbcorp/orb-python/issues/26)) ([9a25d2f](https://github.com/orbcorp/orb-python/commit/9a25d2f07d4fd5b18ab2702240a4c470c680715d))
* **client:** improve file upload types ([#3](https://github.com/orbcorp/orb-python/issues/3)) ([91b3d5c](https://github.com/orbcorp/orb-python/commit/91b3d5c4b383f2ccc1fad7209ad834aeeecaf96e))
* **client:** improve retry behaviour ([#6](https://github.com/orbcorp/orb-python/issues/6)) ([04d94d2](https://github.com/orbcorp/orb-python/commit/04d94d22b7ad214ba748f0a1722b67d5b756e5c8))
* **client:** support passing BaseModels to request params at runtime ([#27](https://github.com/orbcorp/orb-python/issues/27)) ([e8d0844](https://github.com/orbcorp/orb-python/commit/e8d08448ab25e34955f3ae5ca2501565cbe2d192))
* **github:** include a devcontainer setup ([#25](https://github.com/orbcorp/orb-python/issues/25)) ([fc96155](https://github.com/orbcorp/orb-python/commit/fc961559403ad78cb144c348635afbf00410640d))
* **package:** add classifiers ([#16](https://github.com/orbcorp/orb-python/issues/16)) ([fa652f3](https://github.com/orbcorp/orb-python/commit/fa652f3a4b68afb1204c4f6c0f74b00b39f1b9af))


### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#28](https://github.com/orbcorp/orb-python/issues/28)) ([ad6ebef](https://github.com/orbcorp/orb-python/commit/ad6ebefccc8e1cb178b0cc394103ff646a130d72))
* **client:** include more detail in error messages ([#12](https://github.com/orbcorp/orb-python/issues/12)) ([7b64c85](https://github.com/orbcorp/orb-python/commit/7b64c851f6825ec8d2e2f8fcc6174f88f3676d59))
* rename customer.credits.ledger.create_entry_by_exteral_id and RequestValidationErrors ([#9](https://github.com/orbcorp/orb-python/issues/9)) ([bd8dbe9](https://github.com/orbcorp/orb-python/commit/bd8dbe9335a24ff0830d7dad90676fa1d55202d0))


### Chores

* **internal:** minor restructuring of base client ([#15](https://github.com/orbcorp/orb-python/issues/15)) ([550d18c](https://github.com/orbcorp/orb-python/commit/550d18c72e0eb2c06dc83329f07d207a6cf2b0de))
* **internal:** require explicit overrides ([#11](https://github.com/orbcorp/orb-python/issues/11)) ([4dab0a6](https://github.com/orbcorp/orb-python/commit/4dab0a6da2d4992046c6a125b460bd21fb26cd10))


### Documentation

* improve to dictionary example ([#7](https://github.com/orbcorp/orb-python/issues/7)) ([3dac2fd](https://github.com/orbcorp/orb-python/commit/3dac2fd2595e1e2b62f85f284daa4c519998942d))

## 1.27.0 (2023-10-20)

Full Changelog: [v1.26.0...v1.27.0](https://github.com/orbcorp/orb-python/compare/v1.26.0...v1.27.0)

### Features

* **init:** initial commit ([33d4af6](https://github.com/orbcorp/orb-python/commit/33d4af66059edfeffd6b39f058867d1babfd8fa9))


### Chores

* correct version ([58bb98d](https://github.com/orbcorp/orb-python/commit/58bb98df611c05e4b89fb5c2e4a1d7a99dbb312e))


### Documentation

* improve code examples ([927512a](https://github.com/orbcorp/orb-python/commit/927512a8d90168348136c312527b816344ec3a88))
