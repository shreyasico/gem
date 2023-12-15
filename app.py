from flask import Flask, render_template, request, jsonify
import subprocess
import shlex
import amazon
import flipkart
import gem
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prices', methods=['POST'])
def get_prices():
    product_name = request.form.get('product_name')

    # Run the scripts and capture the output
    try:
        amazon_price = subprocess.check_output(['/opt/homebrew/bin/python3', '/Users/shreyashivratriwar/gem/amazon.py', product_name], text=True)
        flipkart_price = subprocess.check_output(['/opt/homebrew/bin/python3', '/Users/shreyashivratriwar/gem/flipkart.py', product_name], text=True)
        gem_price = subprocess.check_output(['/opt/homebrew/bin/python3', '/Users/shreyashivratriwar/gem/gem.py', product_name], text=True)
        
        # Assuming your scripts print the prices, you can extract them here
        # Note: Make sure to modify your scripts to print the prices or return them in a specific format

        return jsonify({
            'amazon_price': amazon_price,
            'flipkart_price': flipkart_price,
            'gem_price': gem_price
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'})



if __name__ == '__main__':
    app.run(debug=True)
