from instant_prompt_box import InstantPromptBox

def main():
    """InstantPromptBox の使用方法の例"""

    # InstantPromptBox の初期化
    instant_prompt_box = InstantPromptBox(prompts_path="./prompts")

    # プロンプトの読み込み
    prompt = instant_prompt_box.load_prompts(prompt_name="zoltraak_prompt_aaaa")

    # 変数の展開
    variables = {"name": "Alice", "age": 30}
    expanded_prompt = instant_prompt_box.expand_variables(prompt=prompt, variables=variables)

    # プロンプトの出力
    instant_prompt_box.output_prompt(prompt=expanded_prompt, output_file="output.txt")

if __name__ == "__main__":
    main()
# 
# このプログラムは、以下の手順で InstantPromptBox を使用しています。
# 
# 1. `InstantPromptBox` クラスのインスタンスを作成し、`prompts_path` を指定してプロンプトファイルの場所を指定します。
# 2. `load_prompts` メソッドを使って、`zoltraak_prompt_aaaa.md` ファイルからプロンプトを読み込みます。
# 3. `expand_variables` メソッドを使って、プロンプト内の変数を `name` と `age` の値に展開します。
# 4. `output_prompt` メソッドを使って、展開されたプロンプトを `output.txt` ファイルに出力します。
# 
# この例では、`prompts` ディレクトリ内に `zoltraak` フォルダがあり、その中に `zoltraak_prompt_aaaa.md` ファイルが存在すると仮定しています。`zoltraak_prompt_aaaa.md` ファイルには、`{{name}}` や `{{age}}` などの変数が含まれているとします。
# 
# このプログラムを実行すると、`output.txt` ファイルに、`zoltraak_prompt_aaaa.md` ファイルの内容が変数が展開された状態で出力されます。
# 
# この例は、InstantPromptBox の基本的な使用方法を示しています。InstantPromptBox の機能をさらに活用するために、他のプロンプトファイルを読み込んだり、変数をより複雑な方法で展開したりすることができます。