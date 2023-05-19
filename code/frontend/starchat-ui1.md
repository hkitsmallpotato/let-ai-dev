# StarCoder/StarChat UI implementation test

(Experiment to extend the automation from design to actual coding phase using the food ordering and delivery platform as an example)

I didn't have time to fully test this, but for some reason StarChat struggle a lots on this task.

(Output manually cleaned and curated)

As it didn't manage to get something reasonable out, I sampled some of the closer hits.

## Prompts

TODO

Omitted for now as the process is too messy

## Partial answer

**Main page**:

```js
import { Box } from "@chakra-ui/react";

 const Home = () => (
     <Box>
       {/* Page Heading */}
       <Heading size="xl">Welcome To Our Fast Food Restaurant</Heading>

       {/* Navigation Bar*/}
       <Flex justify="space-between" align="center" p={4}>
         <Text fontSize="sm">Home / </Text>
         <Text fontWeight="bold">Food / </Text>
         <Text color="#009CCC">Delivery Status</Text>
       </Flex>

       {/* Main Content Area */}
       <VStack spacing={8}>
         {/* Hero Image & CTA Button  */}
         <HStack justifyContent={"space-around"} alignItems={"stretch"} w={"full"} h={"40vh"} bgGradient="linear(to-r, #7928CA,#FF0080)">
           <Image src="/heroimage.jpg" alt="Hero Image"/>

           <Button variant={"solid"} colorScheme={"teal"} rounded={"md"} px={6} py={3}>
             Place Order Now
           </Button>

         </HStack>

         {/* Category Buttons  */}
         <HStack justifyContent={"flex-start"} wrap={"wrap"}>
           {[ "Main Courses", "Side Orders","Beverages"].map((category) => (
               <Tag key={category}>{category}</Tag>
           ))}
         </HStack>

         {/* Food Items List  */}
         <SimpleGrid columns={{base: 1, md: 2}} gap={10}>
           {[...Array(10)].map((_, index) => (
                 <Card key={index}>
                   <Image boxSize={'250px'} objectFit='cover' src={`https://source.unsplash.com/random/${Math.floor(
                      Math.random() * 100
                    )}?sig=${index}`} />

                   <VStack mt={2} ml={2}>
                     <Text textAlign={'left'}>{`Item ${index}`}</Text>

                     <Text
                       opacity={0.6}
                       noOfLines={2}
                       overflow={'hidden'}
                       whiteSpace={'nowrap'}
                     >{`Description about Item ${index}. Some more text here.`}</Text>

                     <HStack justifyContent={'flex-end'} alignItems={'baseline'}>
                       <Text>${`${Math.round(
                         Math.random() * 100
                       )}.${String(Math.round(Math.random() * 10)).padStart(
                         2,
                         '0'
                       )}`}/person</Text>

                       <Spacer />

                       <IconButton icon={<AddIcon />} aria-label="add to cart" />
                     </HStack>
                   </VStack>

                 </Card>
           ))}
         </SimpleGrid>


       </VStack>

     </Box>
 );

 export default Home;
```

**Food option component (Using ChakraUI + step by step)**:

Show me the code to implement the “Food Option” UI component using React + Chakra UI + react hook. Include code for API calls and behavior for the searching/filtering.

----

Here’s sample code implementing the “Food Option” UI component described above using React, Chakra UI, and React Hook Form:

1. Import required libraries at the beginning of your file:
```js
import { useState } from 'eact'; 
import axios from 'axios';  
import { Button, Input, Flex, Box, Heading} from '@chakra-ui/core'  
```
2. Define state variables (filterOptions, filteredData):
```js
const [filterOptions, setFilterOptions] = useState({category: '', minPrice: null, maxPrice:null});  
const [filteredData, setFilteredData] = useState([]);   
```
3. Create function handleFilterChange() which will update the value of filterOptions when any input field changes its value:
```js
  const handleFilterChange= e => {  
      let newFilterOption={...filterOptions}; 
      //update the corresponding property based on event target id
      switch(e.target.id) {  
        case 'category':  
          newFilterOption['category'] = e.target.value; 
          break; 
        case 'in_price':
          newFilterOption['minPrice']= parseInt(e.target.value); 
          break;
        case 'ax_price':
           newFilterOption['maxPrice']=parseInt(e.target.value); 
           break; 
       default:
         return false;
       };  
     console.log("new filter",newFilterOption ); 
     setFilterOptions(newFilterOption);}    
```
4. Call this function inside `<Input />` components `onChange` attribute whenever there is change in values :
```js
     <Box>
        <label htmlFor="category">Category:</label>
        <Select defaultValue={'All'} size='sm' width={{base:'80%',md:"60%"}} id="category" onChange={(event)=>handleFilterChange(event)}>
            <option value={"All"}>All</option> 
            <option value={"Main Courses"}>Main Courses </option>  
            <option value={"Side Dishes"}> Side Dishes </option>   
            <option value={"Desserts"}> Desserts </option>   
        </Select>
    </Box>

    <Box mt={4}>
        <label htmlFor="min_price">Min Price ($):</label>
        <Input type="number" step="any" placeholder="Enter minimum price..." id="min_price"onChange={(event)=>handleFilterChange(event)}/>
    </Box>

    <Box mt={4}>
        <label htmlFor="max_price">Max Price ($):</label>
        <Input type="number" step="any"placeholder="Enter maximum price..." id="max_price"onChange={(event)=>handleFilterChange(event)}/>
    </Box>
```
5. Use `useEffect()` hook to make api call after every time filterOptions object gets updated. You need to pass all these parameters to get filtered data properly. Also you may add error handling here too. Inside effect part we are calling our backend server where we have created routes for getting filtered data according to given criteria. We are passing response into second parameter of `setFilteredData()`.
```js
useEffect(()=> { 
  async function fetchData(){ 
   try{ 
    const res = await axios.post('http://localhost:5000/api/v1/menu', {...filterOptions });  
    setFilteredData(res.data.meals);  
   }catch(err){ 
    alert(`Something went wrong while fetching filtered data`);  
   }  
  } 
  fetchData();},[filterOptions]); 
```
6. Finally map over filteredData array to show cards containing details about individual meal.
```js
<Flex wrap="wrap">
    {filteredData && filteredData.map((meal)=>(
        <Card key={meal._id} p={4} my={4} shadow="lg" borderWidth="1px">
            <Image src={meal.image}/>
            <Heading fontSize="xl">{meal.name}</Heading>
            <Text>${meal.price}</Text>
        </Card>)
    )}
</Flex>
```
This way

(Network Interruption)

**Food option component (low level)**:

Here’s sample JSX code implementing the proposed components from your requirements:

1. Filter component (JSX):
```js
<div className="filter">
  <label htmlFor="category">Category:</label>
  <select id="category" value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)}>
    {categories && categories.map((categ) => (<option key={categ._id}>{categ.name}</option>))}
  </select>

  <label htmlFor="priceRangeMin">Price Range Min ($):</label>
  <input type="number" min="0" max="999999" step=".01" id="priceRangeMin" value={minPrice} 
    onChange={(e) => setMinPrice(+e.target.value)} />
  
  <label htmlFor="priceRangeMax">Price Range Max ($):</label>
  <input type="number" min="0" max="999999" step=".01" id="priceRangeMax" value={maxPrice} 
    onChange={(e) => setMaxPrice(+e.target.value)} />

  <button onClick={() => applyFilters()}>Apply Filters</button>
</div>
```
2. Grid component (JSX):
```js
{filteredItems? 
  <>
    <p>{`Displaying ${filteredItems.length}/${items?.length || '...'} results:`}</p>
    <ul style={{display: 'grid', gap: '.5rem', alignItems: 'center'}}>
      {filteredItems.slice(0, numRows * rowsPerPage).map((item) => 
        <li key={item._id}><ItemCard {...item}/></li>)
      }
    </ul>

    {/* Pagination */}
    {(numPages > 1) && 
      <nav aria-label='Page Navigation'>
        <ul
          style={{
            display: 'flex', 
            justifyContent: 'pace-between', 
            paddingInlineStart: '0' 
          }}
        >
          {[...Array(numPages)].map((_, i) => 
            <li 
              key={`page-${i+1}`}
              style={{
                listStyleType: 'none', 
                margin: 0, 
                borderBottomColor: '#ccc', 
                borderBottomWidth: '3px', 
                cursor: 'pointer'
              }}
            ><a href='#' onClick={()=>setCurrPage(i+1)}>{i+1}</a></li>
          )}
        </ul>
      </nav>}
  </> : null}
```
3. Card component (JSX):
```js
const ItemCard = ({ _id, title, imageUrl, price }) => {
  const [showModal, setShowModal] = useState(false);
  return (
    <>
      <article role="dialog" tabIndex="-1" hidden={!showModal}>
       ... modal content here...
      </article>

      <figure>
        <img src={imageUrl} alt={`${title}-image`} width={'100%'} height={'auto'}/>
        <figcaption>${price}</figcaption>
      </figure>
      
      <footer>
        <span role="button" onClick={() => setShowModal(!showModal)}>Order Now!</span>
      </footer>
    </>
  );
};
export default ItemCard;
```
4. SearchBar component (JSX):
```js
<form onSubmit={handleSubmit}>
  <label htmlFor="searchTerm">Search For A Restaurant Or Food Item:</label>
  <input type="text" id="searchTerm" placeholder="Enter restaurant or food item..." required autoFocus 
    value={searchTerm} onChange={handleChange}/>
  <button type="submit"><FaSearch /></button>
</form>
```
5. **API Calls And Behavior**: In this example we will make two separate GET requests one to retrieve all available categories and another to fetch all available food items. We’ll store these data sets locally within our state management system so that we don’t need to call them again unless there has been an update since last time.
When the user first loads the website, we’ll check whether any local storage exists containing previously fetched data. If

(Network Interrupted)
