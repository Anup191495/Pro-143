const YourComponent = () => {
    const [currentArticle, setCurrentArticle] = useState(null);
  
    useEffect(() => {
      getInitialArticle();
    }, []);
  
    const getInitialArticle = async () => {
      try {
        const response = await fetch('https://your-ngrok-subdomain.ngrok.io/get_initial_article');
        const data = await response.json();
  
        if (data.status === 'success') {
          setCurrentArticle(data.article);
        } else {
          alert('No more articles');
        }
      } catch (error) {
        console.error('Error fetching initial article:', error);
      }
    };
  
    const likeArticle = async (contentId) => {
      try {
        const response = await fetch(`http://localhost:5000/like_article/${contentId}`, {
          method: 'POST',
        });
  
        const data = await response.json();
  
        if (data.status === 'success') {
          getInitialArticle();
        } else {
          alert('Failed to like the article');
        }
      } catch (error) {
        console.error('Error liking the article:', error);
      }
    };
  
    const dislikeArticle = async (contentId) => {
      try {
        const response = await fetch(`http://localhost:5000/dislike_article/${contentId}`, {
          method: 'POST',
        });
  
        const data = await response.json();
  
        if (data.status === 'success') {
          getInitialArticle();
        } else {
          alert('Failed to dislike the article');
        }
      } catch (error) {
        console.error('Error disliking the article:', error);
      }
    };
  
  };
  
  export default YourComponent;
  