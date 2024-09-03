import codecs
import shutil
import os
import macos_tags as tags

def make_nth_parent_directory(path, tags_name):
  # ディレクトリを作成
  os.makedirs(path, exist_ok=True)
  tags.add(tags_name, file=path)

def process_string_be(file_name, delimiter):
  # 区切り文字が文字列に含まれているか確認
  if delimiter in file_name:
    # 区切り文字で文字列を分割
    parts = file_name.split(delimiter, 1)
    # 分割された文字列を格納
    result = parts
  else:
    # 区切り文字がない場合の別の処理
    result = "区切りなし"

  return result

def process_string_le(file_name, delimiter):
  # 区切り文字が文字列に含まれているか確認
  if delimiter in file_name:
    # 区切り文字で文字列を分割
    parts = file_name.rsplit(delimiter, 1)
    # 分割された文字列を格納
    result = parts
  else:
    # 区切り文字がない場合の別の処理
    result = "区切りなし"

def chapter(destination_path, input_path, delimiter):
  if_chapter = process_string_le(input_path, delimiter)
      
  # 章があるかないか、ifある、elseない
  if not(isinstance(if_chapter, str)):
    chapter_num = 1
    story_num = 0
    if_chapter[chapter_num] = if_chapter[1][:if_chapter[1].rfind(".txt")]
    if_chapter[story_num] = if_chapter[0] + '.txt'
    make_nth_parent_directory(os.path.join(destination_path, if_chapter[chapter_num]), "章")
    return os.path.join(if_chapter[chapter_num], if_chapter[story_num])
  else:
    return input_path


def check(file_path):
  for i in range(len(file_path)):
    ab_ditrctory = None
    with codecs.open(file_path[i], 'r', encoding = 'utf-8') as story:
      text = story.read()
      
    # ユーザーのホームディレクトリを取得
    home_dir = os.path.expanduser("~")

    # デスクトップのパスを設定
    desktop_path = os.path.join(home_dir, "Desktop")
    
    #作品タイトルの抽出
    #半角アンダーバーがあるときelse、一話だけで　タイトル_話(＿章）.txt　構成。ない場合、if上位が作品名フォルダ。
    file_name = os.path.basename(file_path[i])
    if_title = process_string_be(file_name, "_")
    if isinstance(if_title, str):
      # 一つ上のフォルダを取得
      title_folder = os.path.basename(os.path.dirname(file_path[i]))
      ab_ditrctory = True
    else:
      title_folder = if_title[0]
      file_name = if_title[1]
      
    # 移動元と移動先のパスを設定、小説フォルダまでを設定タグ付け
    destination_path = os.path.join(desktop_path, title_folder)
    make_nth_parent_directory(destination_path, "小説")
    
    #存在すれば章を取得してフォルダを設定、移動先パスの完成とフォルダの完成
    destination_path = os.path.join(destination_path, chapter(destination_path, file_name, "＿"))
    
    # 移動とタグ付け
    shutil.move(file_path[i], destination_path)
    tags.add("本文", file=destination_path)
    
    if ab_ditrctory:
      if not os.listdir(os.path.dirname(file_path[i])):
        try:
          os.rmdir(os.path.dirname(file_path[i]))
        except OSError as e:
          pass
    
    with codecs.open(destination_path, 'w', encoding = 'utf-16') as new_story:
      new_story.write('\ufeff') 
      new_story.write(text)