const ghpages = require('gh-pages');
ghpages.publish('docs', function(err) {
add:true,
branch: 'gh-pages',
mssage: 'Auto-generated commit gh-pages module',
remote:'upstream',
user: {name: 'wearypossum4770', email: 'wearypossum4770@yahoo.com'}
});
