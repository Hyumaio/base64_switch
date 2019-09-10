# @Created Time: 2019.09.10
# @author: hyumaio


import base64
import binascii
import click


@click.command()
@click.option('--encode', '-en', help='base64 encode')
@click.option('--decode', '-de', help='base64 decode')
def main(encode, decode):
    if encode and decode:
        click.echo('仅支持单次 encode/decode！')

    elif encode:
        encode_str = encode
        encode_bytes = encode.encode()  # 传入参数为 string，需要转换为 bytes 进行 base64 操作

        try:
            b64_encode_bytes = base64.b64encode(encode_bytes)
            b64_encode_str = b64_encode_bytes.decode()

            click.echo('参数：{}'.format(encode_str))
            click.echo('encode 结果：{}'.format(b64_encode_str))  # base64 操作得到的结果为 bytes，需要转换为 string 进行显示
        # except UnicodeDecodeError or binascii.Error: # except 捕获多个异常时需将异常放入一个元祖中，不能使用 or 连接
        except (UnicodeDecodeError, binascii.Error):
            click.echo('encode 失败，请检查编码字符串是否合法！')

    elif decode:
        decode_str = decode
        decode_bytes = decode.encode()

        try:
            b64_decode_bytes = base64.b64decode(decode_bytes)
            b64_decode_str = b64_decode_bytes.decode()

            click.echo('参数：{}'.format(decode_str))
            click.echo('decode 结果：{}'.format(b64_decode_str))
        except (UnicodeDecodeError, binascii.Error):
            click.echo('decode 失败，请检查解码字符串是否正确！')

    else:
        click.echo('未检测到参数！')
        click.echo('请使用 --encode/-en 或者 --decode/-de 上传参数！')


if __name__ == '__main__':
    main()
