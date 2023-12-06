# Changelog

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
