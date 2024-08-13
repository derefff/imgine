# Imgine

Imgine is simple Cli tool, that combine images into one output of (N x M) layout, that could be use in raports and articles

## Usage

The only dependency is `Pillow` library

Running program via python:
```bash
python imgine <flags>
```
or if you somehow compile it:
```bash
imgine <flags>
```

| Avaiable flags| description
|-------|--------
|-in [file1 file2 ...]| Pass images files to combine
|-IN | Pass path to directory with images to cobine
|-out| Set name of output image
|-rows| Set number of rows (default 1)
|-cols| Set number of columns (default 2)
|-rows| Set size of gap between images (default 4)

## Future improvements

The tool is quite simple, however in the future I would like to add small improvments:
- make interpreter of `.imgin` files, that would have way more options of editing images/output etc.
- add indexing option, where each image would be labeled (i.e. <a) b) ...>) 

