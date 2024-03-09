import socket

def send_syslog_message(message, server_ip='127.0.0.1', port=514):
    """
    syslogサーバにメッセージを送信します。

    Parameters:
    - message (str): 送信するメッセージ
    - server_ip (str): syslogサーバのIPアドレス
    - port (int): syslogサーバのポート番号
    """
    # UDPソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # メッセージをsyslogサーバに送信
        sock.sendto(message.encode(), (server_ip, port))
        print(f"メッセージを {server_ip}:{port} に送信しました。")
    except Exception as e:
        print(f"メッセージの送信に失敗しました: {e}")
    finally:
        # ソケットを閉じる
        sock.close()

if __name__ == "__main__":
    # テストメッセージ
    test_message = "テストメッセージ"
    send_syslog_message(test_message)
