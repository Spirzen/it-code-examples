const [isPending, startTransition] = useTransition();

const handleSearch = (value) => {
  startTransition(() => {
    setSearchResults(filterData(value));
  });
};

return (
  <div>
    {isPending && <Spinner />}
    <Results data={searchResults} />
  </div>
);
