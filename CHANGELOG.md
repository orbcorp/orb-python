# Changelog

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
