from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

publications = []

@app.route('/')
def home():
    return render_template('home.html', publications=publications)

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'POST':
        book_name = request.form['book_name']
        description = request.form['description']
        price = request.form['price']
        
        # Check if file is uploaded
        if 'book_photo' in request.files:
            book_photo = request.files['book_photo']
            # Save the uploaded file
            if book_photo.filename != '':
                filename = book_photo.filename
                book_photo.save(os.path.join(app.root_path, 'static', 'uploads', filename))
                book_photo_url = f"/static/uploads/{filename}"
            else:
                book_photo_url = ""  # Default photo URL or handle the case where no photo is uploaded
        else:
            book_photo_url = ""  # Default photo URL or handle the case where no photo is uploaded
        
        publications.append({'book_name': book_name, 'book_photo': book_photo_url, 'description': description, 'price': price})
        
        return redirect(url_for('home'))
    
    return render_template('sell.html')

@app.route('/publication/<int:index>')
def publication(index):
    publication = publications[index]
    return render_template('publication.html', publication=publication)

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        website = request.form['website']
        topic = request.form['topic']
        
        # Perform web scraping
        try:
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find content relevant to the topic
            relevant_content = soup.find_all(text=lambda text: text and topic.lower() in text.lower())
            return render_template('scrape_result.html', content=relevant_content)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('scrape_result.html', error=error_message)
    
    return render_template('scrape.html')

@app.route('/analytics')
def analytics():
    # Sample analytics data
    analytics_data = [
        {'month': 'January', 'sales': 100},
        {'month': 'February', 'sales': 120},
        {'month': 'March', 'sales': 90},
        {'month': 'April', 'sales': 110},
        {'month': 'May', 'sales': 130},
        {'month': 'June', 'sales': 150}
    ]
    return render_template('analytics.html', analytics_data=analytics_data)

if __name__ == '__main__':
    app.run(debug=True)
