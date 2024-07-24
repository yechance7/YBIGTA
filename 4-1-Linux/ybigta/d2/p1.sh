#!/bin/bash

# 1. Python 패키지 설치
# requirements.txt 파일에 명시된 패키지 중 설치되지 않은 것이 있다면 설치
if [ -f requirements.txt ]; then
    echo "Checking and installing Python packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt file not found!"
    exit 1
fi

# 2. 현재 실행 중인 check.py 프로세스 종료
echo "Existing process found. Terminating..."
pkill -f check.py

# 3. tmux 세션 확인 및 생성
TMUX_SESSION_NAME="ybigta-linux"
tmux has-session -t $TMUX_SESSION_NAME 2>/dev/null

if [ $? != 0 ]; then
    echo "Creating new tmux session: $TMUX_SESSION_NAME"
    tmux new-session -d -s $TMUX_SESSION_NAME
else
    echo "Tmux session $TMUX_SESSION_NAME already exists."
fi

# 4. tmux 세션에서 check.py 실행
echo "Starting Python script in tmux session: $TMUX_SESSION_NAME"
tmux send-keys -t $TMUX_SESSION_NAME 'python3 check.py' C-m