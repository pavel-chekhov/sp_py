# 1. подтягиваем код
!rm -rf sp_py
!git clone https://github.com/pavel-chekhov/sp_py.git
%cd sp_py

# 2. перезагрузка модуля (чтобы подхватились свежие изменения)
import importlib
import current_time
importlib.reload(current_time)

# 3. запуск
current_time.main()
