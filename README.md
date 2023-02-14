# YoCLI

*open source project, inspired by HeyCLI.com*

## `yo` lets you express in natural language the CLI command you are looking for

### Examples

```
➜  ~ yo kill process by PID

Suggested command:

kill -9 <PID>
```

```
➜  ~ yo list all files in the dir, showing their size in human-readable format

Suggested command:

ls -lh
```

```
➜  ~ yo reencode the video input.avi to mp4, starting from 5 seconds and ending at 25 seconds

Suggested command:

ffmpeg -ss 5 -i input.avi -t 20 -c copy output.mp4
```


You can also ask `yo` to give multiple suggestions by passing the `N <num>` argument:

```
➜  ~ yo N 3 print all filenames of files whose contains contains the string 'yes'

Suggested commands:

grep -lr "yes" *

grep -rl 'yes' .

grep -R "yes" *
```

## Installation

1. Get an OpenAI secret key. You can get one with $18 free credit by signing up at https://openai.com/api/.
2. Clone this repository.
3. Add these two lines to your `.bashrc` (or `.zshrc`, or equivalent):
```
export OAI_SECRET_KEY='xxx'
source /path/to/this/repo/yo.sh
```
## Other notes

Check `yo.py` to see how the prompt is constructed. If anyone finds improvements to the prompt, feel free to make a PR!

Currently `text-davinci-003` is the default model used. Requests tend to use about 100 tokens in total, so at current prices each call should cost about $0.002. That means you should be able to do about 9000 requests before using up the $18 free credit OpenAI gives you!

## Contributing

Just make a PR :)

## Todo

Rewrite the whole thing in pure bash.
